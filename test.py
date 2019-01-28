#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/test_classifier.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 01/30/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. See the example
#          usage below.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Imports classifier function for using pretrained CNN to classify images 
from classifier import classifier 
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
# Defines a dog test image from pet_images folder
image_dir="/Users/abdullahamamun/Downloads/AIPND-revision-master/intropyproject-classify-pet-images/pet_images/"
results = get_pet_labels(image_dir)

# Defines a model architecture to be used for classification
# NOTE: this function only works for model architectures: 
#      'vgg', 'alexnet', 'resnet'  
model = "vgg"
dogfile = "/Users/abdullahamamun/Downloads/AIPND-revision-master/intropyproject-classify-pet-images/dognames.txt"

# Demonstrates classifier() functions usage
# NOTE: image_classication is a text string - It contains mixed case(both lower
# and upper case letter) image labels that can be separated by commas when a 
# label has more than one word that can describe it.
#image_classification = classifier(image_dir, model)

# prints result from running classifier() function
#print("\nResults from test_classifier.py\nImage:", image_dir, "using model:",
      #model, "was classified as a:", image_classification)
classify_images(image_dir,results,model)
adjust_results4_isadog(results,dogfile)
result_stat = calculates_results_stats(results)
#for key, value in results.items():
    #print("key = {} value = {}".format(key,value))


# test adjust_results4_isadog
"""
dogNames = dict()
with open("/Users/abdullahamamun/Downloads/AIPND-revision-master/intropyproject-classify-pet-images/dognames.txt") as f:
 
    for name in f:
        key = name.rstrip()
        dogNames[key] = 1
    
    for key, value in results.items():
        if value[0] in dogNames:
            results[key].append(1)
        else:
            results[key].append(0)
        if value[1] in dogNames:
            results[key].append(1)
        else:
            results[key].append(0)


for key,value in results.items():
    print("Key = {} value = {}".format(key,value))

"""
"""
for key,value in results.items():
    if value[0] in dogNames:
        print("key = {} value = {}  \'pet image is a dog\'".format(key,value))
    else:
        print("key = {} value = {}  \'pet image is not a dog\'".format(key,value))

"""
"""
# calculates_results_stats
results_stats_dic = dict()
numberOfImages = len(results)
numberOfCorrectDogMatches = 0
numberOfDogImages = 0
numberOfCorrectNonDogMatches = 0
numberOfCorrectBreed = 0
for key,value in results.items():
    if results[key][3] == 1 & results[key][4] == 1:
        numberOfCorrectDogMatches += 1
    if results[key][3] == 1:
        numberOfDogImages += 1
    if results[key][3] == 0 & results[key][4] == 0:
        numberOfCorrectNonDogMatches+=1
    if results[key][3] == 1 & results[key][2] == 1:
        numberOfCorrectBreed+=1

numberOfNotDogImages = numberOfImages - numberOfDogImages
pctOfCorrectlyClassifiedDogs = (numberOfCorrectDogMatches/numberOfDogImages)*100
pctOfCorrectlyClassifiedNonDogImages = 0
if numberOfNotDogImages > 0:
    pctOfCorrectlyClassifiedNonDogImages = (numberOfCorrectNonDogMatches/numberOfNotDogImages)*100
pctOfCorrectlyClassifiedDogBreed = (numberOfCorrectBreed/numberOfDogImages)*100
results_stats_dic = dict()
keys = ["n_img","n_dogs_img","n_notdogs_img","n_correct_dogs","n_correct_notdogs","n_correct_breed","pct_correct_dogs","pct_correct_breed","pct_correct_notdogs"]
value = [numberOfImages,numberOfDogImages,numberOfNotDogImages,numberOfCorrectDogMatches,numberOfCorrectNonDogMatches,numberOfCorrectBreed,pctOfCorrectlyClassifiedDogs,pctOfCorrectlyClassifiedDogBreed,pctOfCorrectlyClassifiedNonDogImages]
for idx in range(0,len(keys),1):
    results_stats_dic[keys[idx]] = value[idx]

 
for key,value in results_stats_dic.items():
    print("key = {} ,value = {} ".format(key,value))
"""

"""
print_results 

numberOfImg = len(results)
numberOfDogImg = result_stat["n_dogs_img"]
numberOfNotDogImg = result_stat["n_notdogs_img"]
pctOfCorrectDog = result_stat["pct_correct_dogs"]
pctOfCorrectBreed = result_stat["pct_correct_breed"]
pctOfCorrectNotDog = result_stat["pct_correct_notdogs"]

print("Number of Images = {} \nNumber of Dog Images = {} \nNumber of Not-A Dog Images = {} \nPercentage of Correct Dogs = {} \nPercentage of Correct Breed = {} \nPercentage of Correct Not-A dog = {}".format(numberOfImg,numberOfDogImg,numberOfNotDogImg,pctOfCorrectDog,pctOfCorrectBreed,pctOfCorrectNotDog))
print_incorrect_dogs = True
if print_incorrect_dogs == True:
    for key, value in results.items():
        if sum(results[key][3:]) == 1:
            print("Pet Image Level = {}\nClassifier Lebel = {} ".format(key,value[1]))
    
    

print_incorrect_breed = True
if print_incorrect_breed == True:
    for key,value in results.items():
        if sum(results[key][3:]) == 2 and results[key][2] == 0:
            print("Misclassified Breed's of Dog found:\nPet Image Level = {}\nClassifier Lebel = {} ".format(key,value[1]))

"""      
print_results(results,result_stat,model,True,True)



    
        

    


    
