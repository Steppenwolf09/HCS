from .models import News, Proposal,\
    TelegramUser, Admission, EmployeeType,\
    EmployeeCalling, CounterValue, Contacts

def auth(username):
    if TelegramUser.objects.filter(username=username).last() == None:
        return False
    return True

def get_last_news():
    newsArray=''
    news = News.objects.all()[:3]
    for n in news:
        newsArray+=str(n.title) + '\n ' + str(n.text) + '\n' + '*****************************' + '\n'
    return newsArray

def create_proposal(message):
    user=TelegramUser.objects.filter(username=message.from_user.username).last()
    propos=Proposal.objects.create(description=message.text, user_id=user.id)
    return 'Создано обращение под номером %s. В ближайшее время оно будет рассмотрено' % propos.id

def get_proposals(username):
    user = TelegramUser.objects.filter(username=username).last()
    propos = Proposal.objects.filter(user_id=user.id)
    return propos

def create_admission(kwargs, username):
    user = TelegramUser.objects.filter(username=username).last()
    adm=Admission.objects.create(
        user_id=user.id,
        carNumber=kwargs['carNumber'],
        fio=kwargs['fio'],
        reason=kwargs['comment'],
    )
    return adm

def get_specialities():
    return EmployeeType.objects.all()

def save_employee_calling(mes, employeeId):
    user = TelegramUser.objects.get(username=mes.chat.username)
    emplType=EmployeeType.objects.get(id=employeeId)
    resp=EmployeeCalling.objects.create(
        user_id=user.id,
        employeeType_id=emplType.id
    )
    return resp
def get_counters(username):
    user = TelegramUser.objects.get(username=username)
    counters=CounterValue.objects.get(user_id=user.id)
    return counters

def save_counters(kwargs, username):
    user = TelegramUser.objects.get(username=username)
    obj, created = CounterValue.objects.update_or_create(
        user_id=user.id,
        defaults={
            'coldWater':kwargs['coldWater'],
            'hotWater':kwargs['hotWater'],
        },
    )
    return obj

def get_contacts():
    contacts=Contacts.objects.all()
    usabilityContacts=''
    for i in contacts:
        usabilityContacts+=str(i)
    return usabilityContacts