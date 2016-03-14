def max_toys(prices, rupees):
  #Compute and return final answer over here
  prices.sort()
  answer = 0
  for toy in prices:
    if (rupees - toy >= 0):
      answer += 1
      rupees -= toy
    else:
      return answer
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)