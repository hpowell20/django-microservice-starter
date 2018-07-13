from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic

import random

FACTS = ['A flock of crows is known as a murder',
         'If you lift a kangaroo''s tail off the ground it can''t hop',
         'Bananas are curved because they grow towards the sun',
         'Recycling one glass jar saves enough energy to watch television for 3 hours',
         'The Titanic was the first ship to use the S.O.S signal',
         'An apple, potato, and onion all taste the same if you eat them with your nose plugged']


class RandomFactsView(generic.FormView):
    def get(self, request, *args, **kwargs):
        index = random.randint(0, len(FACTS) - 1)
        random_fact = FACTS[index]
        return JsonResponse({'random_fact': random_fact})
