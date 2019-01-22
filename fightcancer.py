import random
import numpy as np
import sys
import os
import time

##------------------------------------------------------------------------------
class effectors:
    """The attributes include a dictionary of extrinsic and intrinsic effectors,
    such as cigarette smoking, gene mutations, diabetes etc., with their probabilities of causing cancers."""

    #attributes include a dictionary of extrinsic and intrinsic effectors
    def __init__(self, condition):
        self.condition = condition
        self.cancer_list = []
        self.extrinsic_effectors_options = {'0' : [['lung_cancer', random.randint(5, 10)], ['pancreatic_cancer', random.randint(3, 7)], ['stomach_cancer', random.randint(2, 4)], ['colorectal_cancer', random.randint(1, 4)]],
                                            '1' : [['liver_cancer', random.randint(7, 10)], ['skin_cancer', random.randint(5, 9)], ['lung_cancer', random.randint(3, 6)]],
                                            '2' : [['cervical_cancer', random.randint(8, 10)], ['skin_cancer', random.randint(1, 3)]],
                                            '3' : [['stomach_cancer', random.randint(8, 10)], ['colorectal_cancer', random.randint(1, 3)]],
                                            '4' : [['colorectal_cancer', random.randint(5, 10)], ['prostate_cancer', random.randint(1, 6)]],
                                            '5' : [['liver_cancer', random.randint(8, 10)], ['prostate_cancer', random.randint(3, 7)], ['colorectal_cancer', random.randint(2, 5)]],
                                            '6' : [['pancreatic_cancer', random.randint(8, 10)], ['colorectal_cancer', random.randint(5, 7)], ['stomach_cancer', random.randint(1, 3)]],
                                            '7' : [['skin_cancer', random.randint(8, 10)], ['breast_cancer', random.randint(1, 4)]],
                                            '8' : [['pancreatic_cancer', random.randint(8, 10)], ['colorectal_cancer', random.randint(5, 8)]],
                                            '9' : [['breast_cancer', random.randint(5, 10)], ['prostate_cancer', random.randint(5, 10)]]}

    #the function will create the combined list of effectors that were selected
    def cancer_probability(self):
        for i in self.condition:
            if i != ',':
                self.cancer_list.append(self.extrinsic_effectors_options.get(i))
        return(self.cancer_list)

##---------------------------------------------------------------------------------
class cancer_rank:
    """This class includes a rank() method to calculate the probabilities of getting different type of cancers
    based on the Player_info and Effectors. In addition, the attributes in this class include a list cancer subtypes,
    such as lung cancer, liver cancer, breast cancer etc."""

    def __init__(self, effector_list, gender):
        self.cancer_results = {'lung_cancer': 0 , 'breast_cancer': 0, 'prostate_cancer': 0, 'kidney_cancer': 0,
                               'liver_cancer': 0, 'cervical_cancer': 0, 'stomach_cancer': 0, 'pancreatic_cancer': 0,
                               'colorectal_cancer': 0, 'skin_cancer': 0}
        self.max_cancer_score = 0
        self.max_cancer_type = ''
        self.effector_list = effector_list
        self.gender = gender

    #the function is to find the top rank of cancer based on the effectors
    def ranking(self):
        for i in self.effector_list:
            for j in range(len(i)):
                key = i[j][0]
                value = i[j][1]
                if self.gender == 'male' and key != 'breast_cancer' and key != 'cervical_cancer':
                    self.cancer_results[key] += value
                elif self.gender == 'female' and key != 'prostate_cancer':
                    self.cancer_results[key] += value
        for cancer_type, cancer_score in self.cancer_results.items():
            if cancer_score > self.max_cancer_score:
                self.max_cancer_score = cancer_score
                self.max_cancer_type = cancer_type
        return(self.max_cancer_type)

#--------------------------------------------------------------------------------------------
class symptom:
    """The attributes include a dictionary of symptoms of cancer, such as coughing, fatigue,
    weight loss etc., with their probabilities to associate with different stage of cancers."""

    def __init__(self, cancer_type):
        self.cancer_type = cancer_type
        self.valid_number = False
        self.cancer_meta = False
        self.cancer_stages = {'0' : ['stage I', round(random.uniform(0, 2), 2)],
                              '1' : ['stage II', round(random.uniform(2, 8), 2)],
                              '2' : ['stage III', round(random.uniform(8, 20), 2)],
                              '3' : ['stage IV', round(random.uniform(5, 20), 2)]}
        self.symptom_list = {'breast_cancer': ['Lump inside the breat', 'Color of texture change', 'Swelling of breast', 'Bloody discharge'],
                             'lung_cancer' : ['Persistent cough', 'Cough up blood', 'Weight loss', 'Chest and bone pain'],
                             'prostate_cancer' : ['Urinate frequently', 'Weak, dribbling, or interrupted flow of urine', 'Blood in the urine', 'Pain or stiffness in the lower back, hips, pelvis, or thighs'],
                             'kidney_cancer' : ['Blood in the urine', 'A mass (lump) on the side or lower back', 'Weight loss not caused by dieting', 'Fever that is not caused by an infection'],
                             'liver_cancer': ['Loss of appetite and itching', 'Nausea or vomiting', 'An enlarged liver, felt as a mass under the ribs on the right side', 'Yellowing of the skin and eyes'],
                             'cervical_cancer': ['Extremely heavy periods', 'Unusual vaginal discharge', 'Pelvic, back or leg pain', 'Out-of-nowhere weight loss'],
                             'stomach_cancer': ['Feeling bloated after eating', 'evere, persistent heartburn', 'Persistent vomiting', 'Unintentional weight loss'],
                             'pancreatic_cancer': ['Feeling bloated', 'Stools are changing', 'Losing weight and do not know why', 'Yellowing of the skin and eyes'],
                             'colorectal_cancer': ['A change in bowel habits', 'Cramping or belly pain', 'Blood in the stool', 'Weakness and fatigue'],
                             'skin_cancer': ['Skin changes', 'A flat, red spot that is rough, dry, or scaly', 'A skin sore that fails to heal', 'A spot or sore that becomes painful or which bleeds']}
        self.your_cancer_stage = ''

    # function for getting symtoms
    def stage_cal(self):
        self.cancer_symptom = self.symptom_list.get(self.cancer_type)
        print("")
        print("Please select your symptoms: ")
        print("-----------------------------")
        for i in range(len(self.cancer_symptom)):
            print("(" + str(i) +") " + self.cancer_symptom[i])
        print("-----------------------------")

        while self.valid_number == False:
            try:
                self.your_symptom = input("Enter the number of your symptom: ")
                print("")
                if int(self.your_symptom) < 0 or int(self.your_symptom) > 3:
                    print("not a valid number")
                else:
                    self.valid_number = True

            except ValueError:
                print("not a valid number")

        if self.your_symptom == '3':
            self.cancer_meta = True
        self.your_cancer_stage = self.cancer_stages.get(self.your_symptom)
        return(self.your_cancer_stage)

##------------------------------------------------------------------------------------------
class treatment_option:
    """In this class, three functions of therapeutic options are included and listed below.
        Surgical(): the tumor size will return to 0. Meanwhile, it will also run the Recurrence() in the Response class.
        Chemotherapy(): the tumor size will be a linear decrease upon treatment period.
                        This method interact with the class recurrence().
        Target_therapy(): the tumor size only changes when certain conditions are chosen in the effector class
                          and is decreased by dividing random number upon treatment period This method interact with class
                          recurrence()"""

    def __init__(self, symptom_stage):
        self.stage = symptom_stage[0]
        self.size = float(symptom_stage[1])
        self.cancer_meta = False
        self.other_treatment = ''
        self.size_change = [self.size]
        self.index = 0
        self.durg_resistance = False
        self.survivor =  """
                  ,*****/      Congratulations!
                /      /*      You defeat cancer!!!
               *      /**
               *    //*.
               /* ***/
                *****
              ******/
            /***/  ***/
         ./***/     ///**,
          ,*/         /*/
                /
           ****  ,*,  ** *****  ,**   **, ** .**   .**   ****   ****.
          ***.*  ,*,  ** **,,**  **   **  **  **,  **.  ******  **.***
          **     ,*,  ** **. **. ,** ,**  **   **  **  **,  ,** **  **
          .***   ,*,  ** **,***   ** **   **   **.,*,  **.  .** **,**,
            ***. ,*,  ** **,**    **.**   **   ,****   **.  .** ****.
             ,** ,*,  ** **.**,    ***.   **    ****   **,  *** ** **
          ,****. .**,*** **. **    ***    **    .**     ******  ** ,**
          .***.   .****  **. ,*,   .*,    **     **      ***,   **  **

                        """
        self.killed = """
                                %@@@@@@@%
                          @@@@@@@@,     ,&@@@@.
                      #@@@@@@            .    .@@
                    @@@@@@                *@     .@,
                  %@@@@@                     %      @       Cancer win~~~
                 @@@@@                   .           @.
                #@@@@                                 @
                @@@@/                                  @
                @@@@/    (@@@@@@     %@%    @@@@@@     @
                @@@@/     @@   @@     @.    @@   @@    @
                @@@@/     @@   @,     @.    @@@@%@     @
                @@@@/     @@@@@@      @.    @@         @
                @@@@/     @@   @@     @.    @@         @
           @    @@@@/    %@@@   (@@  @@@&  @@@@        @
            @   @@@@/                                  @
            %. @@@@@/                                  @ @@ @,
              @@@@@@/                (,                @ @ @
              ,@@@@@/            @@@   @@              @ @@.
                @@@@/         @@(       &@(  ,@@@@@@.  @@@
                   *@@/&@@ @@%                      ,& @@
                                                                """


        self.dosing_check = False
        while self.dosing_check == False:
            try:
                self.dosing_period = int(input("Please enter dosing period (1-4): "))
                if self.dosing_period > 0 and self.dosing_period < 5:
                    self.dosing_check = True
                else:
                    print("Please enter the dosing period from 1 to 4")
            except ValueError:
                print("not a dosing period")


    def surgical(self):
        self.index += 2
        self.cancer_meta = recurrence().cancer_metastasis()
        self.durg_resistance = recurrence().drug_response()
        if self.stage == 'stage I' or self.stage == 'stage II':
            self.size = 0
            print(self.survivor)
        elif self.stage == 'stage III' or self.stage == 'stage IV':
            self.size = 0
            if self.cancer_meta == True:
                self.other_treatment = input("Please select additional treatment: " + "\n"
                                           + "(1) Chemotherapy" + "\n" + "(2) Target therapy" + "\n")
                if self.other_treatment == '1':
                    if self.durg_resistance == False:
                        print(self.survivor)
                    elif self.durg_resistance == True:
                        print("\n" + "**Treatment has no response**" + "\n")
                        self.retreat()
                        pass
            else:
                print(self.survivor)
        return(self.size_change)

    def chemotherapy(self):
        self.index += 2
        if self.index > 6:
            print("\n" + "**You are too weak for any additional treatment**" + "\n")
            print(self.killed)
            pass
        elif self.size > 0:
            for i in range(self.dosing_period):
                self.durg_resistance = recurrence().drug_response()
                self.treatment_efficacy = round(random.uniform(0, 3), 2)
                if self.durg_resistance == False:
                    self.size -= self.treatment_efficacy
                    self.size = round(self.size, 2)
                    self.size_change.append(self.size)
                    if self.size > 0 and self.index <= 6:
                        self.index -= 1
                        print("\n" + "**Treatment is not completed." + "\n" + "Tumor size: " + str(self.size) + "\n" + "Metastasis: " + str(self.cancer_meta) +  "\n")
                        self.retreat()
                        break
                    else:
                        print(self.survivor)
                        break
                elif self.durg_resistance == True:
                    self.size_change.append(self.size)
                    print("\n" + "**Treatment has no response**" + "\n")
                    self.retreat()
                    break
                elif self.size <= 0:
                    self.size = 0
                    if self.cancer_meta == True:
                        print("\n" + "**Your cancer has metastasized**" + "\n")
                        self.retreat()
                        break
                    else:
                        print(self.survivor)
                        break
                else:
                    print(self.survivor)
                    break

        elif self.size <= 0 and self.durg_resistance == False:
            self.size = 0
            if self.cancer_meta == True:
                print("\n" + "**Your cancer has metastasized**" + "\n")
                self.retreat()
                pass
            else:
                print(self.survivor)
                pass

        elif self.size == 0 and self.stage == 'stage IV':
            for i in range(self.dosing_period):
                self.cancer_meta = recurrence().cancer_metastasis()
                if self.cancer_meta == True:
                    print("\n" + "**Your cancer has metastasized**" + "\n")
                    self.retreat()
                    pass
                else:
                    print(self.survivor)
                    pass
        else:
            print(self.survivor)
            pass
        return(self.size_change)

    def target_therapy(self):
        self.index += 2
        self.cancer_meta = False
        if self.index > 6:
            print("\n" + "**You are too weak for any additional treatment**" + "\n")
            print(self.killed)
            pass
        elif self.size > 0:
            for i in range(self.dosing_period):
                self.durg_resistance = recurrence().drug_response()
                self.treatment_efficacy = round(random.uniform(1, 3), 2)
                if self.durg_resistance == False:
                    self.size /= self.treatment_efficacy
                    self.size = round((self.size - 1), 2)
                    self.size_change.append(self.size)
                    if self.size > 0 and self.index <= 6:
                        self.index -= 1
                        print("\n" + "**Treatment is not completed." + "\n" + "Tumor size: " + str(self.size) + "\n" + "Metastasis: " + str(self.cancer_meta) +  "\n")
                        self.retreat()
                        break
                    else:
                        print(self.survivor)
                        break
                elif self.durg_resistance == True:
                    self.size_change.append(self.size)
                    print("\n" + "**Treatment has no response**" + "\n")
                    self.retreat()
                    break
                elif self.size <= 0:
                    self.size = 0
                    self.cancer_meta = recurrence().cancer_metastasis()
                    if self.cancer_meta == True:
                        print("\n" + "**Your cancer has metastasized**" + "\n")
                        self.retreat()
                        break
                    else:
                        self.cancer_meta == False
                        print(self.survivor)
                        break

                else:
                    print(self.survivor)
                    break

        elif self.size <= 0 and self.durg_resistance == False:
            self.size = 0
            if self.cancer_meta == True:
                print("\n" + "**Your cancer has metastasized**" + "\n")
                self.retreat()
                pass
            else:
                print(self.survivor)
                pass

        elif self.size == 0 and self.stage == 'stage IV':
            for i in range(self.dosing_period):
                self.cancer_meta = recurrence().cancer_metastasis()
                if self.cancer_meta == True:
                    print("\n" + "**Your cancer has metastasized**" + "\n")
                    self.retreat()
                    pass
                else:
                    print(self.survivor)
                    pass
        else:
            print(self.survivor)

        return(self.size_change)


    def retreat(self):
        print("Please select your treatment: ")
        print("-----------------------------")
        print("(1) Chemotherapy")
        print("(2) Target therapy")
        print("-----------------------------")
        self.treatment_choice = input("Please select the your treatment: ")
        if self.treatment_choice == "1":
            self.change = self.chemotherapy()
        elif self.treatment_choice == "2":
            self.change = self.target_therapy()
        else:
            self.retreat()

##------------------------------------------------------------------------------------------
class recurrence:
    """The class induces two functions. drug_response() applies autoregression algorithmn.
    cancer_metastasis() applies random walk algorithmn.  If outcome of function < 0, it will turn
    attribute into “False”. """

    def __init__(self):
        self.alpha = 0.5
        self.sigma = 1
        self.value = 3
        self.meta_value = 0
        self.recur = False
        self.resistant = False

    def drug_response(self):
        self.value = self.alpha * self.value + np.random.normal(scale = self.sigma)
        if self.value < 0:
            self.resistant = True
        return(self.resistant)

    def cancer_metastasis(self):
        self.value = 0 + np.random.normal(scale = 1)
        if self.value < 0:
            self.recur = True
        return(self.recur)

##-------------------------------------------------------------------------------------------
class treatment_period:
    """The class also includes a treatment_monitor() method to plot the changes of tumor sizes upon tumor treatment."""

    def __init__(self, treat_list, graph_title):
        self.x_scale = 3
        self.y_scale = 21
        self.graph = []
        self.y_max = 20
        self.y_min = 0
        self.graph_flat = ''
        self.treat_list = treat_list
        self.graph_title = graph_title

    #plot the result of treatment
    def treatment_monitor(self):
        for i in range(self.y_scale):
            self.graph.append([" "] * 19 * self.x_scale)

        for i in range(len(self.treat_list)):
            if round(self.treat_list[i]) <= 0:
                pass  # this case will show nothing
            else:
                j = int((self.y_scale - 1) - (round(self.treat_list[i] * (self.y_scale - 1) / 20) - round(self.y_min * (self.y_scale - 1) / 20)))
                self.graph[j][i * self.x_scale] = '@'

        # convert map data to string for output
        self.graph_flat = " " * round((20 * self.x_scale + len(str(int(self.y_max))) - len(self.graph_title)) * 0.5) + self.graph_title + '\n'
        for i in range(len(self.graph)):
            row_plot = "".join(self.graph[i]) + "  " + str(round(self.y_max - i)) + "\n"
            self.graph_flat += row_plot
        self.graph_flat += "_" * 19 * self.x_scale + "\n"
        self.graph_flat += "0" + "".join([" " * 2 + str(x) for x in range(1, 10 , 1)]) + "".join([" " * 1 + str(x) for x in range(10, 19 , 1)]) + "  " + "Month"

        print("\n"+self.graph_flat+"\n")

##-------------------------------------------------------------------------------------------
class player_info:
    """The class will acquire the basic information of the player"""

    def __init__(self):

        print('**************************************')
        #patient name
        self.name = input("Please enter your name: ")
        if len(self.name) < 1:
             self.name='anonymous'

        #patient age
        self.valid_number = False
        while self.valid_number == False:
            try:
                self.age = int(input("Please enter your age (0-120): "))
                if self.age < 0 or self.age > 120:
                    print("Your age is not a human age!!!")
                else:
                    self.valid_number = True

            except ValueError:
                print("not a valid number")


        #patient gender
        self.valid_gender = False
        while self.valid_gender == False:
            try:
                self.gender = str(input("Please enter your genetic gender(please type 'Male' or 'Female' only): "))
                self.gender = self.gender.lower()
                if self.gender == 'male' or self.gender == 'female':
                    self.gender = self.gender
                    self.valid_gender = True
                else:
                    print("Are you a human???")

            except ValueError:
                print("not a valid gender")
        print('**************************************')

        #patient effector
        self.valid_effectors = False
        self.extrinsic_effectors = ['Cigarette smoking and particle pollution', 'Hazardous Chemicals', 'Infection with human papillomavirus (HPV)',
                                    'Infection with Helicobacter pylori', 'Obesity', 'Alchohol','Low-fiber, high-fat diet', 'Ultraviolet (UV) radiation',
                                    'Gene mutation-KRAS/BRAF', 'Gene mutation-BRCA1/BRCA2']
        print("")
        print("Please select factors: ")
        print("-----------------------------")
        for i in range(len(self.extrinsic_effectors)):
            print("(" + str(i) +") " + self.extrinsic_effectors[i])
        print("-----------------------------")

        #patient condition
        self.effector_check_list = ['0','1','2','3','4','5','6','7','8','9',',']
        while self.valid_effectors == False:
            try:
                self.condition = input("Please select the environment and habits that fit for you (use ',' to seperate number): ")
                self.effector_check = list(self.condition)
                self.effector_check_comfirm = []
                for i in self.effector_check:
                    if i in self.effector_check_list:
                        self.effector_check_comfirm.append(i)
                        continue
                if self.effector_check == self.effector_check_comfirm:
                    self.valid_effectors = True
                else:
                    print("Please enter number 0-9")

            except ValueError:
                print("not a valid effectors")

        self.cancer = cancer_rank(effectors(self.condition).cancer_probability(), self.gender).ranking()

        #patient tumor stage
        self.size_stage = symptom(self.cancer).stage_cal()

        # print(str(self.size_stage[0]), str(self.size_stage[1]))
        print("\n" + "** You got ["+ self.size_stage[0] + " " + self.cancer + " " + "and size is " + str(self.size_stage[1]) +"], are you ready to fight it? **"+ "\n")

        #treatment option
        self.valid_choice = False
        self.change = []
        self.treatment = ['Surgery', 'Chemotherapy', 'Target therapy']
        print("Please select your treatment: ")
        print("-----------------------------")
        for i in range(len(self.treatment)):
            print("(" + str(i) +") " + self.treatment[i])
        print("-----------------------------")
        while self.valid_choice == False:
            try:
                self.treatment_choice = input("Please select the your treatment: ")
                if self.treatment_choice == "0":
                    self.change = treatment_option(self.size_stage).surgical()
                    self.valid_choice = True
                elif self.treatment_choice == "1":
                    self.change = treatment_option(self.size_stage).chemotherapy()
                    self.valid_choice = True
                elif self.treatment_choice == "2":
                    self.change = treatment_option(self.size_stage).target_therapy()
                    self.valid_choice = True
                else:
                    print("Not a valid treatment option")

            except ValueError:
                print("not a valid treatment option")

# the function to initiate the game
def game_start():
    print("""
                    *,
                  . ..              Welcome to the world of fighting cancer!!!
                ,..,,               You will be the fighter and see how lucky you are to win the battle!!!
               , .*
           **/..*    ..
            (***    ....     .*
           */**    ,. ...,, .,**///**
            ,,,    .,..,,*********///*
             ,...   ,,,*//,*******////.
               ,  ., **(,*******  *////
                 ,...,,**,*******    //*
                  ,...,**/,*****    ////*
                   ..,,**//,******* *////
                   ,.,,***//,********////
                   ...,,**/#/*,******////.
                   ...,,*(,,.**,.*****///
                   ...,,,,,,,.,***..***/*
                   ...,,.    ,..,,,
                   ...,,      ,...,
                  ...,,,       .*Tumor,
                 ..,,,*   *   *,Tumor*,.
                 ..,,*     . ,*Tumor(//,.
                 ,,,*,.......***Tumor/*,(#,,.
                  ..........////*/(*Tumor#/*,***,,.
                  ...  **//****///,(((/((/..           """)
    time.sleep(1.00)
    print('\n' + 'Please get ready for your personal information' + '\n')
    time.sleep(1.00)
    p1 = player_info()
    graph_title = 'The treatment history of ' + p1.name
    treatment_period(treat_list = p1.change, graph_title = graph_title).treatment_monitor()

##----------------------------------------------------------------------------
game_start()
