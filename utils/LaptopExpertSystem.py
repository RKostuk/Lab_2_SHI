# class LaptopExpertSystem:
#     def __init__(self, max_price, work_requirement, cpu_gpu_demand, education_need, gaming_preference):
#         self.max_price = max_price
#         self.work_requirement = work_requirement
#         self.cpu_gpu_demand = cpu_gpu_demand
#         self.education_need = education_need
#         self.gaming_preference = gaming_preference
#
#     def recommend_laptop(self):
#         laptops = {
#             "Бюджетний робочий ноутбук": {"price": 400, "work_requirement": True, "cpu_gpu_demand": False, "education_need": False, "gaming_preference": False},
#             "Універсальний ноутбук для роботи та навчання": {"price": 800, "work_requirement": True, "cpu_gpu_demand": True, "education_need": True, "gaming_preference": False},
#             "Геймерський ноутбук": {"price": 1200, "work_requirement": True, "cpu_gpu_demand": True, "education_need": False, "gaming_preference": True},
#             "Професійний ноутбук для редагування відео": {"price": 1500, "work_requirement": True, "cpu_gpu_demand": True, "education_need": False, "gaming_preference": False},
#             "Ноутбук для великих обсягів даних та аналітики": {"price": 1800, "work_requirement": True, "cpu_gpu_demand": True, "education_need": False, "gaming_preference": False},
#             "Дизайнерський ноутбук з високоякісним дисплеєм": {"price": 1600, "work_requirement": True, "cpu_gpu_demand": True, "education_need": False, "gaming_preference": False},
#             "Мобільний ноутбук для подорожей": {"price": 1000, "work_requirement": False, "cpu_gpu_demand": False, "education_need": False, "gaming_preference": False},
#             "Ноутбук для мультимедійного використання": {"price": 900, "work_requirement": False, "cpu_gpu_demand": False, "education_need": False, "gaming_preference": False},
#             "Легкий та стильний ноутбук": {"price": 700, "work_requirement": False, "cpu_gpu_demand": False, "education_need": False, "gaming_preference": False},
#             "Ноутбук для інтернет-серфінгу та щоденних задач": {"price": 500, "work_requirement": False, "cpu_gpu_demand": False, "education_need": False, "gaming_preference": False}
#         }
#
#         recommended_laptops = []
#         for laptop, specs in laptops.items():
#             if specs["price"] <= self.max_price and specs["work_requirement"] == self.work_requirement \
#                     and specs["cpu_gpu_demand"] == self.cpu_gpu_demand and specs["education_need"] == self.education_need \
#                     and specs["gaming_preference"] == self.gaming_preference:
#                 recommended_laptops.append(laptop)
#
#         if recommended_laptops:
#             return f"Рекомендовані ноутбуки для вас: {', '.join(recommended_laptops)}"
#         else:
#             return "На жаль, ми не можемо підібрати ноутбук з вашими вимогами та бюджетом."
#
# # Зчитування вхідних даних від користувача
# max_price = float(input("Максимальна ціна за ноутбук: "))
# work_requirement = input("Вам потрібен ноутбук щоб працювати? (True/False): ").lower() == "true"
# cpu_gpu_demand = input("Ваша сфера зв'язана з великими навантаженнями на CPU/GPU? (True/False): ").lower() == "true"
# education_need = input("Ноутбук потрібний для навчання? (True/False): ").lower() == "true"
# gaming_preference = input("Чи граєте ви в ігри? (True/False): ").lower() == "true"
#
# # Створення експертної системи і отримання рекомендацій
# expert_system = LaptopExpertSystem(max_price, work_requirement, cpu_gpu_demand, education_need, gaming_preference)
# recommendation = expert_system.recommend_laptop()
# print(recommendation)


# self.laptops = [
#     {'name': f'Laptop{i}', 'usage': random.choice(['Graphic Design', 'Office Work', 'Gaming', 'Software Development']),
#      'budget': random.choice(['High', 'Medium', 'Low']),
#      'specs': {'screen_size': random.choice(['13 inches', '15 inches', '17 inches']),
#                'processor_type': random.choice(['i5', 'i7', 'Ryzen 5', 'Ryzen 7']),
#                'ram_size': random.choice(['8GB', '16GB', '32GB']),
#                'storage_size': random.choice(['256GB SSD', '512GB SSD', '1TB HDD']),
#                'weight': random.choice(['Light', 'Medium', 'Heavy'])},
#      'brand': random.choice(['Dell', 'HP', 'Lenovo', 'Asus', 'Acer'])} for i in range(1, 51)
# ]
import random


class LaptopExpertSystem:
    def __init__(self, count):
        self.count = count
        self.laptops = self.generate_laptop()
        self.user_preferences = {}

    def generate_laptop(self):
        laptops = []
        for i in range(self.count):
            laptop = {'name': f'Laptop{i}',
                      'usage': random.choice(['Graphic Design', 'Office Work', 'Gaming', 'Software Development']),
                      'budget': random.choice(['High', 'Medium', 'Low']),
                      'screen_size': random.choice(['13 inches', '15 inches', '17 inches']),
                      'processor_type': random.choice(['i5', 'i7', 'Ryzen 5', 'Ryzen 7']),
                      'ram_size': random.choice(['8GB', '16GB', '32GB']),
                      'storage_size': random.choice(['256GB SSD', '512GB SSD', '1TB HDD']),
                      'weight': random.choice(['Light', 'Medium', 'Heavy']),
                      'brand': random.choice(['Dell', 'HP', 'Lenovo', 'Asus', 'Acer'])}
            laptops.append(laptop)
        return laptops

    def print_lap(self):
        print(self.laptops)

    def recommend_laptop(self, recommendations):
        matching_laptops = []

        for laptops in self.laptops:
            count = 0
            for key, recc in recommendations.items():
                if laptops[key] == recc:
                    count += 1
            matching_laptops.append({'count': int(count), 'laptop': laptops})
        max_count_dict = None
        max_count_dict = max(matching_laptops, key=lambda x: x['count'])
        if max_count_dict:
            return max_count_dict.get('laptop')
        else:
            return "Sorry, no matching laptops found for your preferences."



        # for category, preference in laptop_data.items():
        #     if category == 'specs':
        #         for spec, value in preference.items():
        #             matching_laptops = [laptop for laptop in matching_laptops if laptop[category][spec] == value]
        #     else:
        #         matching_laptops = [laptop for laptop in matching_laptops if laptop[category] == preference]
        #
        #     if len(matching_laptops) == 1:
        #         selected_laptop = matching_laptops[0]
        #         break
        #     elif len(matching_laptops) == 0:
        #         print(
        #             f"No matching laptops found for the preference: {category} = {preference}. Reverting to the previous preference.")
        #         matching_laptops = self.laptops.copy()
        #
        # if selected_laptop:
        #     print("\nBased on your preferences, we recommend the following laptop:")
        #     return f"{selected_laptop['name']} - {selected_laptop['brand']} - {selected_laptop['specs']}"
        # else:
        #     return "Sorry, no matching laptops found for your preferences."


if __name__ == "__main__":
    expert_system = LaptopExpertSystem(100)
    print(expert_system.recommend_laptop(
        {
            'usage': 'Gaming',
            'budget': 'Low',
            'screen_size': '13 inches',
            'weight': 'Light',
            'brand': 'HP'}
    ))
    # expert_system.recommend_laptop()
