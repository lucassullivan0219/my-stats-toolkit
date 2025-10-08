# my_stats_toolkit/descriptive.py

def calculate_mean(data):
    """
    計算一個數字列表的平均值。
    
    Args:
        data (list): 一個包含數字的列表。
        
    Returns:
        float: 資料的平均值。
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("輸入必須是數字列表。")
    if not data:
        return 0.0
    return sum(data) / len(data)

def calculate_std_dev(data):
    """
    計算一個數字列表的樣本標準差。
    
    Args:
        data (list): 一個包含數字的列表。
        
    Returns:
        float: 資料的樣本標準差。
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("輸入必須是數字列表。")
    
    n = len(data)
    if n < 2:
        return 0.0
    
    mean = calculate_mean(data)
    variance = sum([(x - mean) ** 2 for x in data]) / (n - 1)
    return variance ** 0.5