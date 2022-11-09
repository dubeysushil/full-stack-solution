from django.shortcuts import render, redirect
from .forms import TeamMemberForm
from .models import TeamMember

# Create your views here.


def team_member_list(request):
    context = {'team_member_list':TeamMember.objects.all(), 'count':TeamMember.objects.all().count()}
    return render(request, 'team_member_add/view-team-members.html',context)

def team_member_add(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TeamMemberForm()
            context = {'form':form,'title':'Add a team member', 'subtitle':'Set name, email and role','id':id}
        else:
            member = TeamMember.objects.get(pk=id)
            form = TeamMemberForm(instance=member)
            context = {'form':form,'title':'Edit a team member', 'subtitle':'Edit name, email and role','id':id}
        return render(request, 'team_member_add/add-team-member.html', context)
    else:
        if id == 0:
            form = TeamMemberForm(request.POST)
        else:
            member = TeamMember.objects.get(pk=id)
            form = TeamMemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            if id == 0:
                context = {'form':form,'title':'Add a team member', 'subtitle':'Set name, email and role','id':id}
            else:
                context = {'form':form,'title':'Edit a team member', 'subtitle':'Edit name, email and role','id':id}
            return render(request, 'team_member_add/add-team-member.html', context)
        

def team_member_delete(request, id):
    if id == 0:
        return redirect('/')
    else:
        member = TeamMember.objects.get(pk=id)
        if member.role == 'Admin':
            member.delete()
    return redirect('/')
