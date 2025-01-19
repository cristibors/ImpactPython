from contourpy.util.data import simple

a=[1,1,2,5,8,13,34,35,2,3]
print(a[3])
print(a[a[2]])

tuple_ex=("hola", 5, "test", 4.55, False)

print(tuple_ex[0])

print(tuple_ex + ("New", "data", 1))

simple_array=[1,2,3,4,5,0,2,3,4,5,2,3]
set_array_2= set(simple_array)
print(simple_array)
print(set_array)
print(set_array_2)