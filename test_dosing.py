import dosing
import pandas as pd
import pytest
import numpy as np

def test_df_left_merge():     
    np.random.seed(0)
    # transactions
    left = pd.DataFrame({'transaction_id': ['A', 'B', 'C', 'D'], 
                        'user_id': ['Peter', 'John', 'John', 'Anna'],
                        'city': ['Lima', 'Sofia', 'London', 'Paris'],
                        'value': np.random.randn(4),
                       })
    # users
    right = pd.DataFrame({'user_id': ['Paul', 'Mary', 'John', 'Anna'],
                         'color': ['blue', 'blue', 'red', 
                                            'cyan'],
                        'city': ['Prague', 'Sofia', 'Milan', 'Paris']
                        })
    
    expected = left.merge(right,  on=['user_id','city'], how='left')
    
    #call function
    actual = dosing.df_left_merge(left, right, 'user_id', 'city')
    
    #assert
    assert actual.equals(expected) == True
    
    
def test_df_filter():
    # transactions
    df = pd.DataFrame({'transaction_id': ['A', 'B', 'C', 'D', 'E'], 
                        'user_id': ['Peter', 'John', 'John', 'Anna', 'John'],
                        'city': ['Lima', 'Sofia', 'London', 'Paris', 'Sofia'],
                        'distance': [180, 250, 180, 30, 220],                       
                        'value': [1, 2, 3, 4, 5],
                       })   
    
    expected = pd.DataFrame({'transaction_id': ['B', 'E'], 
                        'user_id': ['John', 'John'],
                        'city': ['Sofia', 'Sofia'],
                        'distance': [250, 220],                       
                        'value': [2, 5],
                       })    
    
    actual = dosing.df_filter(df, df, 'user_id', 'city', 'distance', 'John', 'Sofia', 180)
    assert actual.equals(expected) == True
