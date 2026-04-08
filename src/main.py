COMMON_PASSWORDS=["password","123456","qwerty"]
def check_length(password):
  return len(password) >=8
def has_uppercase(password):
  for char in password:
    if char.isupper():
      return True
  return False
def has_lowercase(password):
  for char in password:
    if char.islower():
      return True
  return False
def has_digit(password):
  for char in password:
    if char.isdigit():
      return True
  return False
def has_special_character(password):
  for char in password:
    if char=="@" or char=="!" or char=="#" or char=="$" or char=="%" or char=="^" or char=="&" or char=="*":
      return True
  return False
def is_common_password(password):
  for i in COMMON_PASSWORDS:
    if password.lower() == i:
      return True
  return False
def calculate_score(password):
  score=0
  if check_length(password) :
    score+=1
  if has_uppercase(password):
    score+=1
  if has_lowercase(password):
    score+=1
  if has_digit(password):
    score+=1
  if has_special_character(password):
    score+=1
  if len(password) >12:
    score+=1
  if is_common_password(password):
    score-=1
  return max(0,score)
def get_strength_rating(score):
  if score <= 2:
    return "Weak"
  elif score <= 4:
    return "Moderate"
  else:
    return "Strong"
def main():
  password=input("Enter a password: ")
  print("Password: ",password)
  print("Length check: ",check_length(password))
  print("Has Upper: ",has_uppercase(password))
  print("Has Lower: ",has_lowercase(password))
  print("Has Digit: ",has_digit(password))
  print("Has Special Characters: ",has_special_character(password))
  print("IS Common Password: ",is_common_password(password))
  print("Score: ",calculate_score(password),"/6")
  print("Rating: ",get_strength_rating(calculate_score(password)))
if __name__ == "__main__":
    main()
