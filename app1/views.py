
















import math
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render



def graph_view(request):
    
    return render(request, 'app1/index.html') 



def calculate(request):
    
    
    if request.method == 'POST':
        equation = request.POST.get('equation')
        x_values = request.POST.get('xValues')
        y_values = request.POST.get('yValues')

        x_values_list = [float(x.strip()) for x in x_values.split(',')]
        y_values_list = [float(y.strip()) for y in y_values.split(',')]
        
        x_new_list = [0]*(len(x_values_list))
        
        for i in range(len(x_values_list)):
            x_new_list[i]=x_values_list[i]

        if equation == '1':
            # your equation 1 calculation logic
            x2 = 0
            xy = 0
            sumx = 0
            sumy = 0
            n = len(x_new_list)
            ynew = [0] * n

            for i in range(len(x_new_list)):
                x_new_list[i] = math.log(x_new_list[i], 10)
                y_values_list[i] = math.log(y_values_list[i], 10)
                sumx = sumx + x_new_list[i]
                sumy = sumy + y_values_list[i]
                x2 = x2 + (x_new_list[i] * x_new_list[i])
                xy = xy + (x_new_list[i] * y_values_list[i])

            b = ((n * xy) - (sumx * sumy)) / ((n * x2) - (sumx * sumx))
            a = (sumy - (b * sumx)) / n
            a = (10 ** a)

            xnew = x_values_list
            for i in range(len(x_values_list)):
                if b > 0:
                    ynew[i] = a * (x_values_list[i] ** (b))
                else:
                    ynew[i] = x_values_list[i] ** (-b)
                    if ynew[i] == 0:
                        ynew[i] = 0.0
                    else:
                        ynew[i] = a * (1 / (x_values_list[i] ** (-b)))
                        
                        
            return JsonResponse({'xValues': x_values_list, 'yValues': ynew, 'Label':'Best Fit Power Function'})
                        
                        
        elif equation == '2':
            
            x2=0
            xy=0
            sumx=0
            sumy=0
            n = len(x_values_list)
            ynew=[0]*n
            for i in range(len(x_values_list)):
                y_values_list[i]=math.log(y_values_list[i])
        
                sumx=sumx+x_values_list[i]
                sumy=sumy+y_values_list[i]
                x2=x2+(x_values_list[i]*x_values_list[i])
                xy=xy+(x_values_list[i]*y_values_list[i])
           
            a = ((sumy*x2)-(sumx*xy))/((n*x2)-(sumx*sumx))
            b = ((n*xy)-(sumx*sumy))/((n*x2)-(sumx*sumx))
            a=(math.e**a)
            
    
            xnew=x_values_list
            for i in range(len(x_values_list)):
                ynew[i]=a*(math.e**(b*x_values_list[i]))
            
            return JsonResponse({'xValues': x_values_list, 'yValues': ynew, 'Label':'Best Fit Exponential Function'})
        
        
        
        
        
        elif equation == '3':
            
            
            
            
            
            x2=0
            x3=0
            x4=0
            x2y=0
            xy=0
            sumx=0
            sumy=0
            n=len(x_values_list)
            ynew=[0]*n
            for i in range(len(x_values_list)):
                
                sumx=sumx+x_values_list[i]
                sumy=sumy+y_values_list[i]
                x2=x2+(x_values_list[i]*x_values_list[i])
                x3=x3+(x_values_list[i]**3)
                x4=x4+(x_values_list[i]**4)
                xy=xy+(x_values_list[i]*y_values_list[i])
                x2y=x2y+(x_values_list[i]*y_values_list[i]*x_values_list[i])
    
           

            mat=[[n, sumx, x2, sumy],[sumx, x2, x3, xy],[x2, x3, x4, x2y]]
    
    
            cal_d=ans(mat)

    
    # Matrix d1 using mat as given in 
    # cramer's rule
            d1 = [[mat[0][3], mat[0][1], mat[0][2]],[mat[1][3], mat[1][1], mat[1][2]], [mat[2][3], mat[2][1], mat[2][2]]]
            cal_d1=ans(d1)
    
    # Matrix d2 using mat as given in 
    # cramer's rule
            d2 = [[mat[0][0], mat[0][3], mat[0][2]], [mat[1][0], mat[1][3], mat[1][2]], [mat[2][0], mat[2][3], mat[2][2]]]
            cal_d2=ans(d2)
    
    # Matrix d3 using mat as given in 
    # cramer's rule
            d3 = [[mat[0][0], mat[0][1], mat[0][3]], [mat[1][0], mat[1][1], mat[1][3]], [mat[2][0], mat[2][1], mat[2][3]]]
            cal_d3=ans(d3)
            if (cal_d != 0):
    
        # mat have a unique solution. 
        # Apply Cramer's Rule
                a = cal_d1 / cal_d
                b = cal_d2 / cal_d
        
        # calculating z using cramer's rule
                c = cal_d3 / cal_d
        
                    # mat have a unique solution. 
            # Apply Cramer's Rule
            a = cal_d1 / cal_d
            b = cal_d2 / cal_d
        
            # calculating z using cramer's rule
            c = cal_d3 / cal_d
        

            for i in range(len(x_values_list)):
                
                ynew[i]=a+(b*x_values_list[i])+(c*x_values_list[i]*x_values_list[i])
                
            

            
            return JsonResponse({'xValues': x_values_list, 'yValues': ynew, 'Label':'Best Fit Parabola'})
            
            
             
        elif equation == '4':
            
            
            x2=0
            xy=0
            sumx=0
            sumy=0
            n=len(x_values_list)
            ynew=[0]*n
            for i in range(len(x_values_list)):
                sumx=sumx+x_values_list[i]
                sumy=sumy+y_values_list[i]
                x2=x2+(x_values_list[i]*x_values_list[i])
                xy=xy+(x_values_list[i]*y_values_list[i])
            a = (sumy*x2)-(sumx*xy)/((n*x2)-(sumx*sumx))
            b = (n*xy)-(sumx*sumy)/(n*x2)-(sumx*sumx)

            
            xnew=x_values_list
            for i in range(len(x_values_list)):
                ynew[i]=xnew[i]*b+a

            return JsonResponse({'xValues': x_values_list, 'yValues': ynew, 'Label':'Best Fit Straight Line'})
            

    return HttpResponse(status=400)



def ans(mat):    
                
    ans= ((mat[0][0] * (mat[1][1] * mat[2][2] -mat[2][1] * mat[1][2])) -(mat[0][1] * (mat[1][0] * mat[2][2] -mat[1][2] * mat[2][0])) +(mat[0][2] * (mat[1][0] * mat[2][1] -mat[1][1] * mat[2][0])))
    return ans
















# Create your views here.




# import matplotlib.pyplot as plt
# import math
# from django.http import JsonResponse,HttpResponse

# from django.shortcuts import render

# def graph_view(request):
#     return render(request, 'app1/index.html') 



# def calculate(request):
    
    
#     if request.method == 'POST':
        
#         equation = request.POST.get('equation')
#         x_values = request.POST.get('xValues')
#         y_values = request.POST.get('yValues')


#         x_values_list = [float(x.strip()) for x in x_values.split(',')]
#         y_values_list = [float(x.strip()) for x in x_values.split(',')]

#         for x_val in x_values_list:
#             if equation == '1':
               
#                 # y_val = x_val
                           
#                 x2=0
#                 xy=0
#                 sumx=0
#                 sumy=0
#                 n=len(x_values_list)
#                 ynew=[0]*n
#                 for i in range(len(x_values_list)):
        
#                     x_values_list[i]=math.log(x_values_list[i],10)
        
#                     y_values_list[i]=math.log(y_values_list[i],10)
#                     sumx=sumx+x_values_list[i]
#                     sumy=sumy+y_values_list[i]
#                     x2=x2+(x_values_list[i]*x_values_list[i])
#                     xy=xy+(x_values_list[i]*y_values_list[i])
    
#                 b = ((n*xy)-(sumx*sumy))/((n*x2)-(sumx*sumx))
#                 a = (sumy-(b*sumx))/n
#                 a=(10**a)
    
#                 xnew=x_values_list
#                 for i in range(len(x_values_list)):
#                     if b>0:
#                         ynew[i]=a*(x_values_list[i]**(b))
#                     else:
#                         ynew[i]=x_values_list[i]**(-b)
#                         if ynew[i]==0:
#                             ynew[i]=0.0
#                         else:
#                             ynew[i]=a*(1/(x_values_list[i]**(-b)))


    
                
                
                
                
                
#         # elif equation == '2':
               
#         #     y_val = x_val * x_val
          

#         #     y_values_list.append(y_val)

      
#         return JsonResponse({'xValues': x_values_list, 'yValues': ynew})

#     return render(request, 'app1/index.html')
