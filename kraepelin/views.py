from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
import random
# Create your views here.

def test_view(request):
    krapelin_test_list = []
    sections = ["Section-A", "Section-B"]

    for section in sections:
        for row_index in range(0, 15):
            number_list = []
            answer_list = []
            over15 = False
            for column_index in range(0, 80):
                random_number_1 = None
                random_number_2 = None  # previous value
                random_number_3 = None  # second last value
                small_num = 3

                if column_index > 0:
                    random_number_2 = number_list[column_index - 1]
                if column_index > 1:
                    random_number_3 = number_list[column_index - 2]

                if column_index % 5 == 3 and not over15:
                    small_num = 6

                if (
                    column_index != 0
                    and column_index % 5 == 4
                    and not over15
                ):
                    small_num = 15 - random_number_2
                    over15 = False

                # if random_number_2 is None and random_number_3 is None:
                random_number_1 = random.randint(small_num, 9)

                # can't have same value has previous value
                # can't have same value has second last value
                while (
                    random_number_1 == random_number_2
                    or random_number_1 == random_number_3
                ):
                    random_number_1 = random.randint(small_num, 9)

                if random_number_2:
                    total = random_number_1 + random_number_2
                    answer = total % 10

                    if column_index % 5 != 4 and total > 14:
                        over15 = True

                    answer_list.append(answer)
                number_list.append(random_number_1)
            krapelin_test_list.append(
                {
                    "number": row_index + 1,
                    "question": number_list,
                    "answer": answer_list,
                    "section": section,
                }
            )
    return JsonResponse(data=krapelin_test_list, safe=False)