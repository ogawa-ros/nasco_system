import nasco_controller
import time
con = nasco_controller.controller()

con.sg_100ghz_1st.set_onoff(0) # (ON, OFF) = (1, 0)
con.sg_100ghz_2nd_upper.set_onoff(0) # (ON, OFF) = (1, 0)
con.sg_100ghz_2nd_lower.set_onoff(0) # (ON, OFF) = (1, 0)
con.sg_200ghz_1st.set_onoff(0) # (ON, OFF) = (1, 0)                                                                              
con.sg_200ghz_2nd_upper.set_onoff(0) # (ON, OFF) = (1, 0)                                                                        
con.sg_200ghz_2nd_lower.set_onoff(0) # (ON, OFF) = (1, 0) 
time.sleep(1)

#con.sg_100ghz_1st.set_freq(17.4452003333) # GHz
#con.sg_100ghz_2nd_upper.set_freq(9.5) # GHz 
#con.sg_100ghz_2nd_lower.set_freq(4) # GHz
con.sg_200ghz_1st.set_freq(18.814) # GHz                                                                                  
con.sg_200ghz_2nd_upper.set_freq(6.6) # GHz                                                                                      
con.sg_200ghz_2nd_lower.set_freq(4.0) # GHz   
time.sleep(1)

con.sg_100ghz_1st.set_power(14) # dBm
con.sg_100ghz_2nd_upper.set_power(20) # dBm
con.sg_100ghz_2nd_lower.set_power(20) # dBm
#con.sg_200ghz_1st.set_power(14) # dBm                                                                                           
#con.sg_200ghz_2nd_upper.set_power(20) # dBm                                                                                     
#con.sg_200ghz_2nd_lower.set_power(20) # dBm   
time.sleep(1)

con.sg_100ghz_1st.set_onoff(1) # (ON, OFF) = (1, 0)
con.sg_100ghz_2nd_upper.set_onoff(1) # (ON, OFF) = (1, 0)                                 
con.sg_100ghz_2nd_lower.set_onoff(1) # (ON, OFF) = (1, 0)  
con.sg_200ghz_1st.set_onoff(1) # (ON, OFF) = (1, 0)                                                                             
con.sg_200ghz_2nd_upper.set_onoff(1) # (ON, OFF) = (1, 0)                                                                       
con.sg_200ghz_2nd_lower.set_onoff(1) # (ON, OFF) = (1, 0)    
