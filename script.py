from utils import *


def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)


amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52,
                 1775.07, 1893.63]

ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]


# Write code here
def get_returns(prices):
    returns = []
    for i in range(len(prices) - 1):
        start_price = prices[i]
        end_price = prices[i + 1]
        log_returns = calculate_log_return(start_price, end_price)

        returns.append(log_returns)

    return returns


amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

x = [display_as_percentage(amazon_return) for amazon_return in amazon_returns]

y = [display_as_percentage(ebay_return) for ebay_return in ebay_returns]

print(x)
print(y)

amazon_returns_year = sum(amazon_returns)
ebay_returns_year = sum(ebay_returns)

print("The annual rate of return of Amazon is ", display_as_percentage(amazon_returns_year))

print("The annual rate of return of Ebay is", display_as_percentage(ebay_returns_year))

print("------")
amazon_returns_var = calculate_variance(amazon_returns)
print(amazon_returns_var)
ebay_returns_var = calculate_variance(ebay_returns)
print(ebay_returns_var)

amazon_returns_stddev = calculate_stddev(amazon_returns)
print(display_as_percentage(amazon_returns_stddev))
ebay_returns_stddev = calculate_stddev(ebay_returns)
print(display_as_percentage(ebay_returns_stddev))
corr_amazon_ebay = calculate_correlation(amazon_returns, ebay_returns)
print(corr_amazon_ebay)
