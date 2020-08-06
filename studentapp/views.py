from django.shortcuts import render, redirect
from studentapp.models import student
from studentapp.form import PostForm

# Create your views here.
def listone(request):
    try:
        unit = student.objects.get(cName='黃楚喬')
    except:
        errormessage = '讀取錯誤'
    return render(request, 'listone.html', locals())

def listall(request):
    students = student.objects.all().order_by('id')
    return render(request, 'listall.html', locals())

def index(request):
    students = student.objects.all().order_by('id')
    return render(request, 'index.html', locals())

def forminitial(request):
    postform = PostForm()
    return render(request, 'forminitial.html', locals())

#--------------------------------------------------------------
def post(request):
    if request.method == 'POST':
        mess = request.POST['username']
    else:
        mess = '表單資料未傳送'
    return render(request, 'post.html', locals())

def post1(request):
    if request.method == "POST":
        cName = request.POST['cName']
        cSex = request.POST['cSex']
        cBirthday = request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone = request.POST['cPhone']
        cAddr = request.POST['cAddr']
        unit = student.objects.create(cName=cName, 
                                      cSex=cSex, 
                                      cBirthday=cBirthday, 
                                      cEmail=cEmail, 
                                      cPhone=cPhone, 
                                      cAddr=cAddr)
        unit.save()
        return redirect('/index/')
    else:
        message = '請輸入資料(資料不做驗證)'
    return render(request, 'post1.html', locals())

def post2(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            cName = postform.cleaned_data['cName']
            cSex = postform.cleaned_data['cSex']
            cBirthday = postform.cleaned_data['cBirthday']
            cEmail = postform.cleaned_data['cEmail']
            cPhone = postform.cleaned_data['cPhone']
            cAddr = postform.cleaned_data['cAddr']

            #新增一筆資料
            unit = student.objects.create(cName=cName, 
                                          cSex=cSex, 
                                          cBirthday=cBirthday, 
                                          cEmail=cEmail, 
                                          cPhone=cPhone, 
                                          cAddr=cAddr)
            unit.save()
            message = '已儲存...'
            return redirect('/index/')
        else:
            message = '驗證碼錯誤'
    else:
        message = '姓名、性別、生日必須輸入'
        postform = PostForm()
    return render(request, 'post2.html', locals())

def delete(request, id=None):
    if id != None:
        if student.objects.filter(id=id).exists():
            title = '資料刪除頁面'
            h2_value = '刪除編號 ' + id
            index = '再次輸入欲刪除編號 : '
            button_value = '確定刪除'
            if request.method == 'POST':
                if request.POST['del_id'] == id:
                    unit = student.objects.get(id=id)
                    unit.delete()
                    return redirect('/index/')
                else:
                    message = '讀取錯誤 請重新輸入'
        else:
            id = None
            message = '查無此id，請重新輸入'
            title = '選擇刪除編號'
            h2_value = '選擇刪除編號'
            index = '請輸入欲刪除編號 : '
            button_value = '選擇'
            #return redirect('/delete/')
            return render(request, 'delete.html', locals())
    else:
        title = '選擇刪除編號'
        h2_value = '選擇刪除編號'
        index = '請輸入欲刪除編號 : '
        button_value = '選擇'
        if request.method == 'POST':
            '''
            try:
                unit = student.objects.get(id=request.POST['del_id'])
                return redirect('/delete/' + request.POST['del_id'])
            except:
                message = '查無此id，請再次輸入'
            '''
            try:
                if student.objects.filter(id=request.POST['del_id']).exists():
                    return redirect('/delete/' + request.POST['del_id'])
                else:
                    message = '查無此id，請再次輸入'
            except:
                message = '請輸入數字!!'

    return render(request, 'delete.html', locals())

def edit(request, id=None):
    if id != None:      #從index頁面進入 or 有輸入id且存在者
        if student.objects.filter(id=id).exists():
            title = '編號 ' + id + ' 修改頁面'
            h2_value = '編號 ' + id + ' 修改'

            #if request.method == 'POST':
            #request.method 必須要是傳送狀態(如submit)，才能使用
            #在非傳送狀態時，request.method皆為'GET'
            unit = student.objects.get(id=id)
            
            """ 
            從資料庫提出來的Date會是年月日格式
            而模型的DateField要求的輸入格式是以'-'分隔
            故需做轉換，以避免傳送錯誤格式
            """
            str_cBirthday = str(unit.cBirthday)
            str_cBirthday.replace('年', '-')
            str_cBirthday.replace('月', '-')
            str_cBirthday.replace('日', '-')
            unit.cBirthday = str_cBirthday
            
            if request.method == 'POST':
                unit.cName = request.POST['cName']
                unit.cSex = request.POST['cSex']
                unit.cBirthday = request.POST['cBirthday']
                unit.cEmail = request.POST['cEmail']
                unit.cPhone = request.POST['cPhone']
                unit.cAddr = request.POST['cAddr']
                unit.save()
                return redirect('/index/')
            
        else:
            id = None
            message = '查無此id，請重新輸入'
            title = '選擇修改編號'
            h2_value = '選擇修改編號'
            index = '請輸入欲修改編號 : '
            button_value = '選擇'
            return render(request, 'edit.html', locals())
            
    else:               #從網址進入
        title = '選擇修改編號'
        h2_value = '請輸入欲修改的編號'
        index = '請輸入欲修改編號 : '
        button_value = '選擇'
        if request.method == 'POST':
            try:
                if student.objects.filter(id=request.POST['edit_id']).exists():
                    return redirect('/edit/' + request.POST['edit_id'])
                else:
                    message = '查無此id，請再次輸入'
            except:
                message = '請輸入數字!!'

    return render(request, 'edit.html', locals())