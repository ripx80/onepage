import hashlib
import os
from django.core.files.storage import FileSystemStorage

#~ class HashedStorage(FileSystemStorage):
    #~ def _save(self, name, content):
        #~ if self.exists(name):
            #~ self.delete(name)
        #~ return super(HashedStorage, self)._save(name, content)
#~
    #~ def get_available_name(self, name):
        #~ return name



def md5_file(chunks):
    md5 = hashlib.md5()
    for data in chunks:
        md5.update(data)
    return md5.hexdigest()

def hashed_upload_to(field_name, path='images/'):
    def upload_to(instance, filename):
        name = md5_file(getattr(instance, field_name).chunks())
        dot_pos = filename.rfind('.')
        ext = filename[dot_pos:][:10].lower() if dot_pos > -1 else '.unknown'
        name += ext
        return os.path.join(path, name)
    return upload_to
