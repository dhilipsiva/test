getDigits = (value) ->
  digits = []
  while value > 0
    lastDigit = value % 10
    digits.splice 0, 0, lastDigit
    value = parseInt value / 10
  digits

getMultipliedArray = (digits) ->
  multipliedArray = []
  multiplyWithThree = false
  for digit in digits
    val = digit
    if multiplyWithThree
      val *= 3
    multipliedArray.push val
    multiplyWithThree = !multiplyWithThree
  multipliedArray

calculateISBN13 = (value) ->
  digits = getDigits value
  multipliedArray = getMultipliedArray digits
  sumOfMultipled = multipliedArray.reduce (a, b) -> a + b
  mod10 = sumOfMultipled % 10
  lastDigit = 10 - mod10
  isbn13 = value * 10 + lastDigit
  alert isbn13

calculateButton = document.getElementById "calculate"

calculateButton.onclick = ->
  isbn12Input = document.getElementById "isbn12"
  isbn12 = parseInt isbn12Input.value
  if isNaN isbn12
    alert "Please enter a valid number"
  else
    calculateISBN13 isbn12
