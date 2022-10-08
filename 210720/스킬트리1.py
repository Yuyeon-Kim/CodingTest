def solution(skill, skill_trees):
    return len(list(filter(lambda st:skill.find(''.join([s for s in list(st) if s in skill]))==0, skill_trees)))