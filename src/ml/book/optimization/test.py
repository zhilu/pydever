import optimization

s=[1,4,3,2,7,3,6,3,2,4,5,3]

optimization.printschedule(s);


print (optimization.schedulecost(s));

domain=[(0,9)]*(len(optimization.people)*2)
s=optimization.randomoptimize(domain,optimization.schedulecost)
print (optimization.schedulecost(s));
optimization.printschedule(s);

s=optimization.hillclimb(domain,optimization.schedulecost)
print (optimization.schedulecost(s));
optimization.printschedule(s);

 
s=optimization.annealingoptimize(domain,optimization.schedulecost)
print (optimization.schedulecost(s));
optimization.printschedule(s);

s=optimization.geneticoptimize(domain,optimization.schedulecost)
print (optimization.schedulecost(s));
optimization.printschedule(s);