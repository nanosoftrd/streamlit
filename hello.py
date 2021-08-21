# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('nanosoftrd')
st.write('This is a example paragraph : my name is mayur. company name is nanosoftrd')
#st.write(pd.DataFrame({'roll no':[1,2,3,4],'name':['mayur','shubham','pratham','aniket']}))
df=pd.DataFrame({'roll no':[1,2,3,4],'name':['mayur','shubham','pratham','aniket']})
df
chart_data = pd.DataFrame(
    
                                np.random.randn(20,3),
                                columns=['a','b','c']
    
    
                        )

st.line_chart(chart_data)
