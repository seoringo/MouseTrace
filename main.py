from record import RecordMouseMovement
from repro import ReproductionMouse


def btn_record():
    '''記録ボタンを押された'''
    record = RecordMouseMovement()
    record.start()

def btn_repro():
    '''再現ボタンが押された'''
    repro = ReproductionMouse()
    repro.get_content()

btn_record()