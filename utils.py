import json


def load_candidate(f):
    """Загружает кандидатов из файла в список"""
    raw_json = f.read()
    candidates = json.loads(raw_json)
    return candidates


def get_all(candidates):
    """Покажет нам всех кандидатов"""
    candidate_list = ''
    for candidate in candidates:
        candidate_list += f"{candidate['name']}\n"
    return candidate_list


def get_by_id(id):
    """Вернет нам кандидата по id"""
    for candidate in candidates:
        if candidate['id'] == id:
            return candidate


def get_by_name(name):
    """Вернет нам кандидатов по имени"""
    candidate_list = []
    for candidate in candidates:
        if name.lower() in (candidate['name']).lower():
            candidate_list.append(candidate)
    return candidate_list


def get_by_skill(skills):
    """Вернет нам кандидатов по навыку"""
    candidate_list = []
    for candidate in candidates:
        if skills.lower() in (candidate['skills']).lower():
            candidate_list.append(candidate)
    return candidate_list


#Читаем файл с JSON
with open('candidates.json', 'r', encoding='utf-8') as f:
    candidates = load_candidate(f)

#print(len(candidates))
#print(get_by_id(2))
#print(get_by_name('lo'))
#print(get_by_skill('python'))