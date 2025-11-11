#Name: Bavesh Hariharan
#id  :   24100729



def main(csvfile):
    student_data = {}
    non_student_data = {}
    platform_engagement = {}
    student_age_income = []
    non_student_age_income = []
    engagement_student = []
    engagement_non_student = []

    with open(csvfile, 'r') as file:
        next(file)  
        for line in file:
            data = line.strip().split(',')
            user_id = data[0].lower()
            age = int(data[1])
            time_spent_hour = int(data[3])
            engagement_score = float(data[4])
            profession = data[9].lower()  
            platform = data[5].lower()  
            income = int(data[10])

            #op1 finding whether the profession is student or not
            if profession == "student":
                student_data[user_id] = [age, time_spent_hour, engagement_score]
            else:
                non_student_data[user_id] = [age, time_spent_hour, engagement_score]

            #op2 appending values 
            if platform not in platform_engagement:
                platform_engagement[platform] = []
            platform_engagement[platform].append(time_spent_hour * engagement_score / 100)

            #op3 appending age, income in their respective lists just checking the profession= student 
            if profession == "student":
                student_age_income.append((age, income))
            else:
                non_student_age_income.append((age, income))

            #op4 now appending the engagement time in the engagement student list.
            engagement_time = float(data[3])
            if profession == 'student':
                engagement_student.append(engagement_time)
            else:
                engagement_non_student.append(engagement_time)

    #op1 setting op1 = student data and non student data so that they will return the desired op
    OP1 = student_data, non_student_data

    #op2 calculating the standard deviation by this formula
    for platform, engagement_times in platform_engagement.items():
        total = sum(engagement_times)
        avg = total / len(engagement_times) if engagement_times else 0
        mean = sum(engagement_times) / len(engagement_times)
        squared_diff_sum = sum((x - mean) ** 2 for x in engagement_times)
        variance = squared_diff_sum / len(engagement_times)
        standard_deviation = variance ** 0.5
        platform_engagement[platform] = [total, round(avg, 4),round(standard_deviation, 4) ]# last OP2 value wrong did a graceful termination.
    OP2 = platform_engagement

    #op3 assigning the final ans for OP3 as a list called OP3
    student_age = [x[0] for x in student_age_income]
    student_income = [x[1] for x in student_age_income]
    student_similarity = cosine_similarity(student_age, student_income)

    non_student_age = [x[0] for x in non_student_age_income]
    non_student_income = [x[1] for x in non_student_age_income]
    non_student_similarity = cosine_similarity(non_student_age, non_student_income)
    OP3 = [round(student_similarity, 4), round(non_student_similarity, 4)]

    #op4 calculating the Cohen’s d test
    mean_student = sum(engagement_student) / len(engagement_student)
    mean_non_student = sum(engagement_non_student) / len(engagement_non_student)
    n1 = len(engagement_student)
    n2 = len(engagement_non_student)
    std_dev1 = sum((x - mean_student) ** 2 for x in engagement_student) / (n1 - 1)
    std_dev2 = sum((x - mean_non_student) ** 2 for x in engagement_non_student) / (n2 - 1)
    pooled_var = ((n1 - 1) * std_dev1 + (n2 - 1) * std_dev2) / (n1 + n2 - 2)
    pooled_sd = pooled_var ** 0.5
    cohens_d = (mean_student - mean_non_student) / pooled_sd
    OP4 = 'error message' #OP4 is wrong so did a graceful termination

    return OP1, OP2, OP3, OP4


# OP3 We created a new fn called cosine similarity to calculate the values for OP3 
def cosine_similarity(vec1, vec2):
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    magnitude1 = sum(x ** 2 for x in vec1) ** 0.5
    magnitude2 = sum(y ** 2 for y in vec2) ** 0.5
    if magnitude1 == 0 or magnitude2 == 0:
        return 0  
    return dot_product / (magnitude1 * magnitude2)

