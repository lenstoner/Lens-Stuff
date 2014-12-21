import pickle
import shelve

#out_file = open('C:/PythonData/mydata.txt','w')
#out_file.write("Hello\n")
#out_file.write("world")
#out_file.flush()
#out_file.close()

## Append data to a file.
#out_file = open('C:/PythonData/mydata.txt','a')
#out_file.writelines("\nGoodbye!")
#out_file.close()

## Pickle data to a string variable
#letters = ['a', 'b', 'c']
#pickled_letters = pickle.dumps(letters)
#print(pickled_letters)

## Convert pickled data to original form.
#unpickled_letters = pickle.loads(pickled_letters)
#print(unpickled_letters)

## Pickle data to a file
#outfile = open('C:/PythonData/pickledata.txt', 'wb')
#letters = ['a', 'b', 'c']
#pickled_letters = pickle.dump(letters, outfile)
#outfile.close()

# Write data in original form to file.
#infile = open('C:/PythonData/pickledata.txt', 'rb')
#file_data = pickle.load(infile)
#infile.close()
#print(file_data)

## Shelve data
#DBfile = shelve.open('C:/PythonData/letters.txt', 'c')
#DBfile['vowels'] = ['a', 'e', 'i', 'o', 'u']
#DBfile['end'] = ['x', 'y', 'z']
#DBfile.sync()
#DBfile.close()

DBfile = shelve.open('C:/PythonData/letters.txt', 'c')
print(list(DBfile.keys()))
DBfile.close()