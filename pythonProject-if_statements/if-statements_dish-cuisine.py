dish=input("Enter a dish name: ")

filipinoCuisine=['adobo', 'sinigang']

if dish in filipinoCuisine:
    print('Filipino')

elif dish=='samgyupsal' or dish=='bibimbap':
    print('Korean')

elif dish=='sushi' or dish=='tempura':
    print('Japanese',dish)

else:
    print('that dish is neither Filipino nor Korean nor Japanese')


