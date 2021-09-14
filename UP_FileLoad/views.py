import hashlib
import os
import shutil
import time
import zipfile

from django.forms import models
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
from django.utils.encoding import escape_uri_path
from openpyxl import Workbook

# Create your views here.
from Django_Project.settings import BASE_DIR

from Django_Project.funtion import check_dir
from UP_FileLoad.models import Files_Info


def up_fl(request):
    """
    上传文件
    :param request:
    :return:
    """
    if request.method == "POST":
        file_name = request.POST.get("file_name", None)
        file = request.FILES.get('file', None)
        address = request.META["HTTP_X_FORWARDED_FOR"] if "HTTP_X_FORWARDED_FOR" in request.META else request.META[
            "REMOTE_ADDR"]
        machine_code = request.environ.get("HTTP_USER_AGENT", None)
        if file:
            file_name = file_name if file_name else file.name
            file_dir_route = os.path.join(BASE_DIR, 'UP_FileLoad', 'files', 'o_files')
            file_name_no = os.path.splitext(os.path.basename(file_name))[0]
            o_file_route = os.path.join(file_dir_route, file_name_no)
            file_dir = os.path.join(o_file_route, file.name)
            check_dir(file_dir)
            with open(file_dir, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            s_file = os.path.join(file_dir_route, file_name).replace(os.path.splitext(file_name)[1], '.zip').replace(
                'o_files', 's_files')
            zip_files(o_file_route, s_file)
            file_md5 = GetFileMd5(s_file)
            md5_fn = s_file.replace(file_name_no, file_md5)
            if not os.path.exists(md5_fn):
                os.renames(s_file, md5_fn)
            else:
                os.remove(s_file)
            time.sleep(5)
            try:
                shutil.rmtree(o_file_route)
            except BaseException as e:
                print("权限不足".format(e))
            fi_dict = {
                'file_name': file_name,
                'md5_fn': file_md5,
                'ip_address': address,
                'machine_code': machine_code,
            }
            Files_Info.objects.create(**fi_dict)
            state = 200
            content = "上传成功"
        else:
            state = 403
            content = "上传失败"
    else:
        state = 404
        content = "请使用POST请求"
    return JsonResponse({"state": state, "content": content})


def zip_files(dir_path, zip_path):
    """
    :param dir_path: 需要压缩的文件目录
    :param zip_path: 压缩后的目录
    :return:
    """
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as f:
        for root, _, file_names in os.walk(dir_path):
            for filename in file_names:
                f.write(os.path.join(root, filename), filename)


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    cal_md5 = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        cal_md5.update(b)
    f.close()
    return cal_md5.hexdigest()


def dl_fl(request):
    """
    下载文件
    :param request:
    :return:
    """
    file_id = request.GET.get("id") if request.method == "GET" else request.POST.get("id")
    print(file_id)
    file_info = None
    try:
        file_info = Files_Info.objects.get(id=file_id)
    except BaseException as e:
        ''.format(e)
    finally:
        if file_info:
            file = open(os.path.join(BASE_DIR, 'UP_FileLoad', 'files', 's_files', '{0}.zip'.format(file_info.md5_fn)),
                        'rb')
            # response = FileResponse(file)
            response = HttpResponse(file, content_type='application/zip')
            file_name = str(file_info.file_name)
            response['Content-Disposition'] = "attachment; filename={0}".format(escape_uri_path(file_name))
            return response
        else:
            state = 403
            content = "不存在此文件"
            return JsonResponse({"state": state, "content": content})


def sl_fl(request):
    """
    查看文件信息
    :param request:
    :return:
    """
    request_state = request.GET if request.method == "GET" else request.POST
    limit = request_state.get("limit", 0)
    offset = request_state.get("offset", 10)
    files_info = Files_Info.objects.all()[limit:offset]
    files_info_dict = dict()
    for fi in files_info:
        files_info_dict[fi.id] = fi.file_name
    state = 200
    content = "查询成功"
    return JsonResponse(
        {"state": state, "content": content, 'limit': limit, 'offset': offset, 'files_info_dict': files_info_dict})
