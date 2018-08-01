import random
from math import cos,exp
import subprocess
import os
import time
#def f(x):
#    fin = -1
#    for i in xrange(len(x)):
#        fin *= cos(x[i])*(exp(1)**(-(x[i]-3.14)**2))
#    return fin

DELAY_MAX = 1.18e-11


def updateFront(swarm, oldFront):
    newFront = list()
    for i in range(len(oldFront)):
	for j in range(len(swarm)):
	    cost_n = list()
	    cost_n = func5(swarm[j].position_i)
	    if (cost_n[0] <= DELAY_MAX and cost_n[1] <= DELAY_MAX and cost_n[2] <= DELAY_MAX and cost_n[3] <= DELAY_MAX and cost_n[4] <= DELAY_MAX and cost_n[5] <= DELAY_MAX):
		cost_o = list()
		cost_o = func5(oldFront[i].position_i)
		if(cost_n[6] <= cost_o[6] and cost_n[7] <= cost_o[7] and cost_n[8] <= cost_o[8] and cost_n[9] <= cost_o[9] and cost_n[10] <= cost_o[10] and cost_n[11] <= cost_o[11] and cost_n[12] <= cost_o[12] and cost_n[13] <= cost_o[13]):
		    newFront.append(swarm[j])
    if len(newFront) == 0:
	return oldFront
    return newFront

def func5(ind):
    cost = list()
    delay = list()
    leakage = list()
    delay = func2(ind)
    leakage = func1(ind)
    cost.extend(delay)
    cost.extend(leakage)
    return cost

def func1(ind):
    with open('tfa_leak_25,1.sp','r') as file:
        data=file.readlines()
        #ind=str(ind)
        #print(len(data))
        #print(data[39])
        #print("lol",len(data))
        #data[27]= '.param wp='+str(ind[0])+'n'+'\n'
        #data[28]= '.param wn='+str(ind[1])+'n'+'\n'
	#data[29]= '.param lp='+str(ind[2])+'n'+'\n'
	#data[30]= '.param ln='+str(ind[3])+'n'+'\n'

	data[34]='Mp1    1   nodea   vdd   vdd   pmos  l=' + str(ind[1]) + 'n ' + 'w=' + str(ind[0]) + 'n\n'
        data[35]='Mp2    1   nodeb   vdd   vdd   pmos  l=' + str(ind[3]) + 'n ' + 'w=' + str(ind[2]) + 'n\n'
        data[36]='Mp3    nodecon nodec   1   vdd   pmos l=' + str(ind[5]) + 'n ' + 'w=' + str(ind[4]) + 'n\n'
        data[37]='Mn1    5   nodea   gnd   gnd   nmos  l=' + str(ind[7]) + 'n ' + 'w=' + str(ind[6]) + 'n\n'
        data[38]='Mn2    5   nodeb   gnd   gnd   nmos  l=' + str(ind[9]) + 'n ' + 'w=' + str(ind[8]) + 'n\n'
        data[39]='Mn3    nodecon nodec   5   gnd   nmos l=' + str(ind[11]) + 'n ' + 'w=' + str(ind[10]) + 'n\n'
        data[40]='Mp4    4   nodea   vdd   vdd   pmos  l=' + str(ind[13]) + 'n ' + 'w=' + str(ind[12]) + 'n\n'
        data[41]='Mp5    nodecon nodeb   4   vdd   pmos  l=' + str(ind[15]) + 'n ' + 'w=' + str(ind[14]) + 'n\n'
        data[42]='Mn4    nodecon nodeb   node4   gnd   nmos l=' + str(ind[17]) + 'n ' + 'w=' + str(ind[16]) + 'n\n'
        data[43]='Mn5    node4   nodea   gnd   gnd   nmos l=' + str(ind[19]) + 'n ' + 'w=' + str(ind[18]) + 'n\n'
        data[44]='Mp6    2   nodea   vdd   vdd   pmos  l=' + str(ind[21]) + 'n ' + 'w=' + str(ind[20]) + 'n\n'
        data[45]='Mp7    2   nodeb   vdd   vdd   pmos l=' + str(ind[23]) + 'n ' + 'w=' + str(ind[22]) + 'n\n'
        data[46]='Mp8    2   nodec   vdd   vdd   pmos l=' + str(ind[25]) + 'n ' + 'w=' + str(ind[24]) + 'n\n'
        data[47]='Mp9    nodes0n nodecon 2   vdd   pmos l=' + str(ind[27]) + 'n ' + 'w=' + str(ind[26]) + 'n\n'
        data[48]='Mn6    3   nodea   gnd   gnd   nmos l=' + str(ind[29]) + 'n ' + 'w=' + str(ind[28]) + 'n\n'
        data[49]='Mn7    3   nodeb   gnd   gnd   nmos l=' + str(ind[31]) + 'n ' + 'w=' + str(ind[30]) + 'n\n'
        data[50]='Mn8    3   nodec   gnd   gnd   nmos l=' + str(ind[33]) + 'n ' + 'w=' + str(ind[32]) + 'n\n'
        data[51]='Mn9    nodes0n nodecon 3   gnd   nmos l=' + str(ind[35]) + 'n ' + 'w=' + str(ind[34]) + 'n\n'
        data[52]='Mp10   9   nodea   vdd   vdd   pmos  l=' + str(ind[37]) + 'n ' + 'w=' + str(ind[36]) + 'n\n'
        data[53]='Mp11   8   nodeb   9   vdd   pmos    l=' + str(ind[39]) + 'n ' + 'w=' + str(ind[38]) + 'n\n'
        data[54]='Mp12   nodes0n nodec   8   vdd   pmos l=' + str(ind[41]) + 'n ' + 'w=' + str(ind[40]) + 'n\n'
        data[55]='Mn10   7   nodea   gnd   gnd   nmos  l=' + str(ind[43]) + 'n ' + 'w=' + str(ind[42]) + 'n\n'
        data[56]='Mn11   6   nodeb   7   gnd   nmos    l=' + str(ind[45]) + 'n ' + 'w=' + str(ind[44]) + 'n\n'
        data[57]='Mn12   nodes0n nodec   6   gnd   nmos  l=' + str(ind[47]) + 'n ' + 'w=' + str(ind[46]) + 'n\n'
        data[58]='Mp13   nodeco  nodecon vdd   vdd   pmos l=' + str(ind[49]) + 'n ' + 'w=' + str(ind[48]) + 'n\n'
        data[59]='Mn13   nodeco  nodecon gnd   gnd   nmos l=' + str(ind[51]) + 'n ' + 'w=' + str(ind[50]) + 'n\n'
        data[60]='Mp14   nodes0  nodes0n vdd   vdd   pmos l=' + str(ind[53]) + 'n ' + 'w=' + str(ind[52]) + 'n\n'
        data[61]='Mn14   nodes0  nodes0n gnd   gnd   nmos  l=' + str(ind[55]) + 'n ' + 'w=' + str(ind[54]) + 'n\n'


    with open('tfa_leak_25,1.sp','w') as file:
         file.writelines(data)

    from subprocess import call
    call(["hspice64", "tfa_leak_25,1.sp"])

    with open('tfa_leak_25,1.ms0','r') as file:
         data=file.readlines()

#    list_of_elements=list()
#    final_list=list()
#    list_of_elements.extend([float(x) for x in data[8].split()])
#    final_list.append(list_of_elements[1])

    final_list=list()
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[14].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[21].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[28].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[35].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[42].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[49].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[56].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[63].split()])
    final_list.append(list_of_elements[0])
    
#    s = 0
#    for i in final_list:
#	s += i
#    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV",s)
#    return(s/8)
    return final_list

def func2(ind):
    with open('tfa_del_25,1.sp','r') as file:
        data=file.readlines()
   #     data[57]='Mp1   nodez   nodea   vdd!   vdd!   pmos  w=' + str(ind[0]) + 'n' + ' l=' + str(ind[2]) + 'n \n'
   #     data[58]='Mn1   nodez   nodea   gndd!   gndd!   nmos  w='+  str(ind[1]) + 'n' + ' l=' + str(ind[3]) + 'n \n'


	data[33]='Mp1    1   nodea   vdd   vdd   pmos  l=' + str(ind[1]) + 'n ' + 'w=' + str(ind[0]) + 'n\n'
	data[34]='Mp2    1   nodeb   vdd   vdd   pmos  l=' + str(ind[3]) + 'n ' + 'w=' + str(ind[2]) + 'n\n'
	data[35]='Mp3    nodecon nodec   1   vdd   pmos l=' + str(ind[5]) + 'n ' + 'w=' + str(ind[4]) + 'n\n'
	data[36]='Mn1    5   nodea   gnd   gnd   nmos  l=' + str(ind[7]) + 'n ' + 'w=' + str(ind[6]) + 'n\n'
	data[37]='Mn2    5   nodeb   gnd   gnd   nmos  l=' + str(ind[9]) + 'n ' + 'w=' + str(ind[8]) + 'n\n'
	data[38]='Mn3    nodecon nodec   5   gnd   nmos l=' + str(ind[11]) + 'n ' + 'w=' + str(ind[10]) + 'n\n'
	data[39]='Mp4    4   nodea   vdd   vdd   pmos  l=' + str(ind[13]) + 'n ' + 'w=' + str(ind[12]) + 'n\n'
	data[40]='Mp5    nodecon nodeb   4   vdd   pmos  l=' + str(ind[15]) + 'n ' + 'w=' + str(ind[14]) + 'n\n'
	data[41]='Mn4    nodecon nodeb   node4   gnd   nmos l=' + str(ind[17]) + 'n ' + 'w=' + str(ind[16]) + 'n\n'
	data[42]='Mn5    node4   nodea   gnd   gnd   nmos l=' + str(ind[19]) + 'n ' + 'w=' + str(ind[18]) + 'n\n'
	data[43]='Mp6    2   nodea   vdd   vdd   pmos  l=' + str(ind[21]) + 'n ' + 'w=' + str(ind[20]) + 'n\n'
	data[44]='Mp7    2   nodeb   vdd   vdd   pmos l=' + str(ind[23]) + 'n ' + 'w=' + str(ind[22]) + 'n\n'
	data[45]='Mp8    2   nodec   vdd   vdd   pmos l=' + str(ind[25]) + 'n ' + 'w=' + str(ind[24]) + 'n\n'
	data[46]='Mp9    nodes0n nodecon 2   vdd   pmos l=' + str(ind[27]) + 'n ' + 'w=' + str(ind[26]) + 'n\n'
	data[47]='Mn6    3   nodea   gnd   gnd   nmos l=' + str(ind[29]) + 'n ' + 'w=' + str(ind[28]) + 'n\n'
	data[48]='Mn7    3   nodeb   gnd   gnd   nmos l=' + str(ind[31]) + 'n ' + 'w=' + str(ind[30]) + 'n\n'
	data[49]='Mn8    3   nodec   gnd   gnd   nmos l=' + str(ind[33]) + 'n ' + 'w=' + str(ind[32]) + 'n\n'
	data[50]='Mn9    nodes0n nodecon 3   gnd   nmos l=' + str(ind[35]) + 'n ' + 'w=' + str(ind[34]) + 'n\n'
	data[51]='Mp10   9   nodea   vdd   vdd   pmos  l=' + str(ind[37]) + 'n ' + 'w=' + str(ind[36]) + 'n\n'
	data[52]='Mp11   8   nodeb   9   vdd   pmos    l=' + str(ind[39]) + 'n ' + 'w=' + str(ind[38]) + 'n\n'
	data[53]='Mp12   nodes0n nodec   8   vdd   pmos l=' + str(ind[41]) + 'n ' + 'w=' + str(ind[40]) + 'n\n'
	data[54]='Mn10   7   nodea   gnd   gnd   nmos  l=' + str(ind[43]) + 'n ' + 'w=' + str(ind[42]) + 'n\n'
	data[55]='Mn11   6   nodeb   7   gnd   nmos    l=' + str(ind[45]) + 'n ' + 'w=' + str(ind[44]) + 'n\n'
	data[56]='Mn12   nodes0n nodec   6   gnd   nmos  l=' + str(ind[47]) + 'n ' + 'w=' + str(ind[46]) + 'n\n'
	data[57]='Mp13   nodeco  nodecon vdd   vdd   pmos l=' + str(ind[49]) + 'n ' + 'w=' + str(ind[48]) + 'n\n'
	data[58]='Mn13   nodeco  nodecon gnd   gnd   nmos l=' + str(ind[51]) + 'n ' + 'w=' + str(ind[50]) + 'n\n'
	data[59]='Mp14   nodes0  nodes0n vdd   vdd   pmos l=' + str(ind[53]) + 'n ' + 'w=' + str(ind[52]) + 'n\n'
	data[60]='Mn14   nodes0  nodes0n gnd   gnd   nmos  l=' + str(ind[55]) + 'n ' + 'w=' + str(ind[54]) + 'n\n'

    print("PRINTING DATA", data)

    with open('tfa_del_25,1.sp','w')as file:
        file.writelines(data)

    from subprocess import call
    call(["hspice64","tfa_del_25,1.sp"])

    with open('tfa_del_25,1.mt0','r') as file:
        data=file.readlines()
    final_list=list()

#    strings=data[4].split()
#    final_list.append(float(strings[2]))

    final_list.extend([float(x) for x in data[4].split()])
    tp = data[5].split()
    final_list.append(float(tp[0]))
    final_list.append(float(tp[1]))
#    s = 0
#    for i in final_list:
#	s += i
#	if i > DELAY_MAX :
#		return 1
#    print("UUUUUUUUUUUUUUUUUUUUUUUUUUU", s)
#    return(s/6)
    return final_list

def func3(ind):
    return 0.5 * (float(func1(ind)) + float(func2(ind)))


#func1([360,180])

class Particle:
    def __init__(self,pp):
        self.pos_best_i=list()
        self.velocity_i=list()
        self.position_i=list()
        self.err_i=list()
        self.err_best_i=list()

        for i in xrange(0,num_dim):
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(pp[i])

#    def evaluate(self,costFunc):
#        self.err_i=costFunc(self.position_i)
#        if self.err_i < self.err_best_i or self.err_best_i==-1:
#            self.pos_best_i=self.position_i
#            self.err_best_i=self.err_i

    def evalPareto(self, costFunc):
	self.err_i = costFunc(self.position_i)
	if len(self.err_best_i) == 0:
	    self.pos_best_i = self.position_i
	    self.err_best_i = self.err_i
	else:
	    flag = 0
	    for i in range(0, 6):
		if(self.err_i[i] > DELAY_MAX):
		    flag = 1
	    for i in range(6, 14):
		if(self.err_i[i] > self.err_best_i[i]):
		    flag = 1
	    if flag == 0:
		self.pos_best_i = self.position_i
		self.err_best_i = self.err_i

    def upd_vel(self,pos_best_g):
        w=0.5
        c1=1
        c2=2

        for i in xrange(0,num_dim):
            print ("=========================================", self.pos_best_i[i])
            #print (self.pos_best_i[i])
            r1=random.random()
            r2=random.random()
            #print(type(self.pos_best_i[i]),"l,llllllllllllllllllllllllll")
            vel_cognitive=c1*r1*(self.pos_best_i[i] - self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social
            print("++++++++++++++++++++++",self.velocity_i[i])

    def upd_pos(self,bounds):
        for i in range(0,num_dim):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]

            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]
            print("@@@@@@@@@@@@@@@@@@@", self.position_i[i])

class pso():
    def __init__(self,costFunc,pp,bounds,totpar,maxiter):
        global num_dim
        swarm=list()
        num_dim=len(pp)
        err_best_g=list()
        pos_best_g=list()

        for i in xrange(0,totpar):
            swarm.append(Particle(pp))
        for i in xrange(0, len(swarm)):
            print (i, "--->>>>", swarm[i].pos_best_i)
        i=0
	paretoFront = list()
	paretoFront = swarm
        while i < maxiter:
	    print("ITERATION -", i)
            for j in xrange(0,totpar):
                swarm[j].evalPareto(costFunc)
                #if swarm[j].err_i < err_best_g or err_best_g == -1:
                #    print ("----------------------")
                #    print(swarm[j].position_i)
                #    pos_best_g=list(swarm[j].position_i)
                #    err_best_g=(swarm[j].err_i)	
	    leader = random.randint(0, len(swarm) - 1)
	    err_best_g = func5(swarm[leader].position_i)
	    pos_best_g = swarm[leader].position_i

            for j in xrange(0,totpar):
                swarm[j].upd_vel(pos_best_g)
                swarm[j].upd_pos(bounds)
            i+=1
	    paretoFront = updateFront(swarm, paretoFront)

#        print ('OUTPUT')
#       time.sleep(2)
#       print (pos_best_g,str('p'))
        #a=(func3(pos_best_g))
        print('OUTPUT')
# print (pos_best_g,str('p'))
        print (pos_best_g)
        #print a
        # print err_best_g


#pso(f,initial,bounds,totpar=1500,maxiter=40)

file =open("fa_leak_25,1.sp",'r')
f=file.readlines()
#print("FILE tleakage_not.sp===============", f)

#wp=f[27][10:-2]
#lp=f[29][10:-2]
#wn=f[28][10:-2]
#ln=f[30][10:-2]

wp1=f[34][47:52]
lp1=f[34][39:43]
wp2=f[35][47:52]
lp2=f[35][39:43]
wp3=f[36][48:53]
lp3=f[36][40:44]
wn1=f[37][47:52]
ln1=f[37][39:43]
wn2=f[38][47:52]
ln2=f[38][39:43]
wn3=f[39][48:53]
ln3=f[39][40:44]
wp4=f[40][47:52]
lp4=f[40][39:43]
wp5=f[41][49:54]
lp5=f[41][41:45]
wn4=f[42][52:57]
ln4=f[42][44:48]
wn5=f[43][50:55]
ln5=f[43][42:46]
wp6=f[44][47:52]
lp6=f[44][39:43]
wp7=f[45][46:51]
lp7=f[45][38:42]
wp8=f[46][46:51]
lp8=f[46][38:42]
wp9=f[47][48:53]
lp9=f[47][40:44]
wn6=f[48][46:51]
ln6=f[48][38:42]
wn7=f[49][46:51]
ln7=f[49][38:42]
wn8=f[50][46:51]
ln8=f[50][38:42]
wn9=f[51][48:53]
ln9=f[51][40:44]
wp10=f[52][47:53]
lp10=f[52][39:43]
wp11=f[53][47:53]
lp11=f[53][39:43]
wp12=f[54][48:54]
lp12=f[54][40:44]
wn10=f[55][47:52]
ln10=f[55][39:43]
wn11=f[56][47:52]
ln11=f[56][39:43]
wn12=f[57][49:54]
ln12=f[57][41:45]
wp13=f[58][50:55]
lp13=f[58][42:46]
wp14=f[59][50:55]
lp14=f[59][42:46]
wn13=f[60][50:55]
ln13=f[60][42:46]
wn14=f[61][51:56]
ln14=f[61][43:47]

file.close()
#initial=[float(wp),float(wn), float(lp), float(ln)]
print(wp1, lp1, wp2, lp2, wp3, lp3, wn1, ln1, wn2, ln2, wn3, ln3, wp4, lp4, wp5, lp5, wn4, ln4, wn5, ln5, wp6, lp6, wp7, lp7, wp8, lp8, wp9, lp9, wn6, ln6, wn7, ln7, wn8, ln8, wn9, ln9, wp10, lp10, wp11, lp11, wp12, lp12, wn10, ln10, wn11, ln11, wn12, ln12, wp13, lp13, wp14, lp14, wn13, ln13, wn14, ln14)
initial=[float(wp1), float(lp1), float(wp2),float(lp2), float(wp3), float(lp3), float(wn1), float(ln1), float(wn2), float(ln2), float(wn3), float(ln3),float(wp4), float(lp4), float(wp5), float(lp5), float(wn4), float(ln4), float(wn5), float(ln5), float(wp6), float(lp6), float(wp7), float(lp7), float(wp8), float(lp8), float(wp9), float(lp9), float(wn6), float(ln6), float(wn7), float(ln7), float(wn8), float(ln8), float(wn9), float(ln9), float(wp10), float(lp10), float(wp11), float(lp11), float(wp12), float(lp12), float(wn10), float(ln10), float(wn11), float(ln11),float(wn12), float(ln12), float(wp13), float(lp13), float(wp14), float(lp14), float(wn13), float(ln13), float(wn14), float(ln14)]  
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",initial)
#exit()
bounds=[(90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50), (90, 1000), (45, 50)] 

pso(func5,initial,bounds,totpar=25,maxiter=200)



