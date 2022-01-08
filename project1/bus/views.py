from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import BusDetails
from . forms import TicketForm
# Create your views here.
def homepage(request):
    return render(request,'home.html')

def booktickets(request):
    if(request.method=='POST'):
        form = TicketForm(request.POST)
        if form.is_valid():
           data = form.cleaned_data
           bus =  BusDetails.objects.all()
           BusDet =[(x.Bus_No,x.Destinations,x.Seats_Available,x.TicketCosts) for x in bus]
           rsg_msg = ""
           form_BusNo = data["BusNo"]
           for ind in range(len(BusDet)):
               each = BusDet[ind]
               if form_BusNo == each[0]:
                   form_destination = data["destination"]
                   form_noofpersons = data["noofpersons"]
                   if form_destination not in each[1]:
                       rsg_msg="Your Destination is wrong"
                       return render(request, 'bookresults.html', context={'msg': rsg_msg})
                   if each[2]<form_noofpersons:
                       rsg_msg="Seats are Not available.You can't book"
                       return render(request, 'bookresults.html', context={'msg': rsg_msg})
                   total_cost = 0
                   index = each[1].split(',').index(form_destination)
                   cost = each[3].split(',')
                   for ticket_cost in cost[:index+1]:
                       total_cost += int(ticket_cost)
                   total_cost = int(cost[index])
                   rsg_msg="Your Ticket is Booked and the cost is {}".format(total_cost*form_noofpersons)
                   bus[ind].Seats_Available-=form_noofpersons
                   bus[ind].save()
                   return render(request, 'bookresults.html', context={'msg': rsg_msg})

           else:
                 rsg_msg = "Invalid BusNo"
                 return render(request,'bookdetails.html',context={'msg':rsg_msg})


    else:
       form = TicketForm()
       return render(request,'booktickects.html',context={'form':form})


