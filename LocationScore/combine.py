import pandas as pd

df1 = pd.read_excel('a_1.xlsx')
df2 = pd.read_excel('a_2.xlsx')
df3 = pd.read_excel('a_3.xlsx')
df4 = pd.read_excel('b_1.xlsx')
df5 = pd.read_excel('b_2.xlsx')
df6 = pd.read_excel('b_3.xlsx')
df7 = pd.read_excel('b_4.xlsx')
df8 = pd.read_excel('b_5.xlsx')
df9 = pd.read_excel('b_6.xlsx')
df10 = pd.read_excel('c_1.xlsx')
df11 = pd.read_excel('c_2.xlsx')
df12 = pd.read_excel('d_1.xlsx')
df13 = pd.read_excel('d_2.xlsx')
df14 = pd.read_excel('d_3.xlsx')
df15 = pd.read_excel('e_1.xlsx')
df16 = pd.read_excel('f_1.xlsx')
df17 = pd.read_excel('g_1.xlsx')
df18 = pd.read_excel('g_2.xlsx')
df19 = pd.read_excel('g_3.xlsx')
df20 = pd.read_excel('i_1.xlsx')
df21 = pd.read_excel('j_1.xlsx')
df22 = pd.read_excel('j_2.xlsx')
df23 = pd.read_excel('k_1.xlsx')
df24 = pd.read_excel('k_2.xlsx')
df25 = pd.read_excel('k_3.xlsx')
df26 = pd.read_excel('k_4.xlsx')
df27 = pd.read_excel('k_5.xlsx')
df28 = pd.read_excel('k_6.xlsx')
df29 = pd.read_excel('l_1.xlsx')
df30 = pd.read_excel('l_2.xlsx')
df31 = pd.read_excel('m_1.xlsx')
df32 = pd.read_excel('m_2.xlsx')
df33 = pd.read_excel('m_3.xlsx')
df34 = pd.read_excel('m_4.xlsx')
df35 = pd.read_excel('m_5.xlsx')
df36 = pd.read_excel('n_1.xlsx')
df37 = pd.read_excel('n_2.xlsx')
df38 = pd.read_excel('n_3.xlsx')
df39 = pd.read_excel('o_1.xlsx')
df40 = pd.read_excel('p_1.xlsx')
df41 = pd.read_excel('p_2.xlsx')
df42 = pd.read_excel('p_3.xlsx')
df43 = pd.read_excel('q_1.xlsx')
df44 = pd.read_excel('r_1.xlsx')
df45 = pd.read_excel('r_2.xlsx')
df46 = pd.read_excel('s_1.xlsx')
df47 = pd.read_excel('s_2.xlsx')
df48 = pd.read_excel('s_3.xlsx')
df49 = pd.read_excel('s_4.xlsx')
df50 = pd.read_excel('s_5.xlsx')
df51 = pd.read_excel('t_1.xlsx')
df52 = pd.read_excel('t_2.xlsx')
df53 = pd.read_excel('t_3.xlsx')
df54 = pd.read_excel('u_1.xlsx')
df55 = pd.read_excel('v_1.xlsx')
df56 = pd.read_excel('v_2.xlsx')
df57 = pd.read_excel('w_1.xlsx')
df58 = pd.read_excel('y_1.xlsx')
df59 = pd.read_excel('z_1.xlsx')


combined_df = pd.concat([df1, df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,df51,df52,df53,df54,df55,df56,df57,df58,df59], ignore_index=True)
combined_df = combined_df.dropna()
combined_df.to_excel('Railway_Station.xlsx', index=False)