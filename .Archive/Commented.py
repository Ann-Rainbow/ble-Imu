# timestamp = rawData([0]) ошибка "TypeError: '_io.TextIOWrapper' object is not callable"
# print(type(timestamp))

#for x in resultX: # Нормально
    #print(type(x))
    #x = int(x) # Нормально
    #print(type(x))
    #print(x)

#for y in resultY:
    #print(type(y))

#print(resultY)
#print(resultX)
# rawData.close()

#X = resultX[:]
#Y = resultY[:]

# for x in (resultY, resultX):
    #listZ.append(resultY.split(' ')) # не вышло
    #listZ.append(resultX) # не вышло
    #listZ.append(resultY, resultX) - only 1 argument must be here, otherwise it's prohibited
    #listZ = list(set(resultY+resultX)) # не работает так, только время прикрепило
    # listZ.append(resultY) # сделало append сначала времени
    # listZ.append(resultX) # затем координаты


    #listZ = resultY + resultX
    #listZ = listZ.append(x) # ошибка AttributeError: 'NoneType' object has no attribute 'append'



# print(listZ)
#print(X)
#print(Y)
# model = LogisticRegression() #Исправить
# model.fit(listZ)


#model.fit(resultX, resultY) # нельзя

#dataset = np.loadtxt(result, delimiter=" ")
# print(dataset)
#x = dataset[:]




#print(dataset)
#x = dataset[1]
#print(x)


# print(dataset[:, :-1])
# print(dataset[:, -1])

# 1,0,0,1
# 1,0,0 - вектор признаков, 1 - результат, второй параметр функции обучения fit
# x = dataset[:, :-1] закомментировала
# y = dataset[:, -1] закомментировала


#svmClass.fit(x) # , y) закомментировала
#svmClass = Classification() закомментировала







# testValues = np.array([[0, 0, 1]], float)  закомментировала
# svmPredict = svmClass.predict(testValues)  закомментировала
# print(svmPredict)  закомментировала

# Save - load Models
# save the model to disk
# filename = 'model.dat'
# pickle.dump(model, open(filename, 'wb'))
#
# ...
#
# load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)