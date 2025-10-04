from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_to_gdrive(file_obj, file_name):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # ✅ file_obj is already a disk file from upload.py
    upload_file = drive.CreateFile({'title': file_name})
    upload_file.SetContentFile(file_obj.name)  # Use filename instead of .read()
    upload_file.Upload()

    return upload_file['id']  # return the Drive file ID

def download_from_gdrive(file_id, save_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(save_path)
    return save_path
