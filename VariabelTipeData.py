#!/usr/bin/env python
# coding: utf-8

# <h1>Variabel dan Tipe Data Python<h1><hr>
# <font color="blue">Beberapa</font> aturan pembuatan variabel di <b>python</b>:
#     
# 

# <ol>
#     <li>Bersifat case sensitif => A != a</li>
#     <li>harus diawali dengan huruf atau karakter _(underscore)</li>
#     <li>Tidak boleh menggunakan spasi</li>
#     <li>Boleh menggunakan angka</li>
# </ol>

# In[3]:


data_int = 10
data_float = 100.9
data_string = '1'
data_bool = True

print(data_int)
print(data_float)
print(data_string)
print(data_bool)


# Untuk mengetahui tipe data dari sebuah variabel gunakan command <b>type</b>

# In[6]:


print(type(data_int))
print(type(data_float))
print(type(data_string))
print(type(data_bool))


# Pada python terdapat proses <b>CASTING</b> yaitu konversi dari sebuah tipe datake tipe yang lain yaitu dengan sintaks <b>tipe_data(nama_variabel)

# In[11]:


int_to_float = float(data_int)
int_to_string = str(data_int)
int_to_bool = bool(data_int)

print("Nilai variabel data_int=",data_int)
print(int_to_float)
print(int_to_string)
print(int_to_bool)


# In[20]:


str_to_int = int(data_string)
str_to_float = float(data_string)
str_to_bool = bool(data_string)

print("Nilai variabel data_string=",data_string)
print(str_to_float)
print(str_to_int)
print(str_to_bool)


# In[22]:


float_to_int = int(data_float)
float_to_string = int(data_float)
float_to_bool = int(data_float)

print("Nilai variabel data_float=",data_float)
print(float_to_int)
print(float_to_string)
print(float_to_bool)


# In[23]:


bool_to_int = int(data_bool)
bool_to_float = int(data_bool)
bool_to_string = int(data_bool)

print("Nilai variabel data_bool=",data_bool)
print(bool_to_int)
print(bool_to_float)
print(bool_to_string)


# In[ ]:


bil1 = input("Isikan bilangan 1")
bil2 = input("Isikan bilangan 2")
hasil_tambah = bil1 + bil2
hasil_bagi = bil1 / bil2
print ("Hasil Penjumlahan",hasil_tambah)
print ("Hasil Pembagian",hasil_bagi)


# In[ ]:




