from App.models import db


class ModelUtil():
    def save(self):
        data = {
            'msg':'ok',
            'status':'201'
        }
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            data['msg'] = str(e)
            data['status']='500'
            return data
        return data