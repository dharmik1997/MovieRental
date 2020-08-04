from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# /customers
# /available-movies/customer_id
# /rent_movie/customer_id/movie_id


# Create your views here.
from .models import Customer


def write_data_to_file(data):
    movieText = ''
    customerText = ''
    for movie in data['movies']:
        movieText += movie['name'] + ',' + str(movie['available']) + '\n'
    with open('movieApp/movies.txt', 'w') as f:
        f.write(movieText.strip())

    for customer in data['customers']:
        customerText += customer['name'] + ',' + customer['age'] + ',' + customer['city'] + ',' + str(
            customer['movie_id']) + '\n '
    with open('movieApp/customers.txt', 'w') as f:
        f.write(customerText.strip())


def get_data_from_files():
    customers = []
    movies = []
    with open('movieApp/customers.txt') as f:
        for line in f.readlines():
            name, age, city, movie_id = line.strip().split(',')
            customers.append({'id': len(customers), 'name': name, 'age': age, 'city': city, 'movie_id': movie_id})
    with open('movieApp/movies.txt') as f:
        for line in f.readlines():
            name, available = line.strip().split(',')
            movies.append({'id': len(movies), 'name': name, 'available': available})
    return {'customers': customers, 'movies': movies}


def all_customers(req):
    # data = get_data_from_files()
    data2 = models.Customer.objects.all()
    print(data2, 'data2')
    print(models.Movie, 'movies')
    return render(req, 'movieApp/customers.html', {'customers': data2})


def available_movies(req, cust_id):
    # data = get_data_from_files()
    data2 = models.Movie.objects.all()
    print(data2)
    return render(req, 'movieApp/available.html', {'movies': data2, 'cid': cust_id})


def rent_movie(req, cid, mid):
    m1 = models.Movie.objects.get(id=mid)
    print(m1, 'Movie m1')
    c1 = models.Customer.objects.get(id=cid)
    print(c1, 'customer c1')
    c1.movies.add(m1)
    print('Customer', c1)
    c1.save()
    m1.avail = False
    m1.save()
    return HttpResponse('movie assigned')


'''
    data = get_data_from_files()
    print(data)
    if  data['movies'][mid]['available'] == 1:
        data['customers'][cid]['movie_id'] = mid
        data['movies'][mid]['available'] = 0
        write_data_to_file(data)
        return HttpResponse('movie assigned')
    else:
        return HttpResponse('movie not available')
'''


def get_detail(req, cid):
    data2 = models.Customer.objects.get(id=cid)
    print('Get detail:', data2)
    return render(req, 'movieApp/customerDetail.html', {'customers': data2})


def add_user(req):
    data2 = models.Customer.objects.all()
    name = req.GET.get('name')
    age = req.GET.get('age')
    city = req.GET.get('city')
    customer1 = Customer(name=name, age=age, city=city)
    # matches = Customer.objects.filter(name__contains=name)
    
    customer1.save()
    return render(req, 'movieApp/customers.html', {'customers': data2})


def unrent(req, cid):
    c1 = models.Customer.objects.get(id=cid)
    print(c1, 'c1')
    m1 = models.Movie.objects.get(id=cid)
    print(m1, 'm1')
    c1.movie = None
    c1.save()
    m1.avail = True
    m1.save()
    return HttpResponse('movie unrented')