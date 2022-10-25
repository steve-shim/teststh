class Const(object):
    def __getattr__(self, name):
        return self[name]

class MmbrStCd(Const):
    SIGN_UP     = 'I'     # 등록
    ACTIVE      = 'A'     # 활동
    DROP_OUT    = 'T'     # 탈퇴
    
print(MmbrStCd.SIGN_UP)