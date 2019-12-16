# --- module import.
import time
import nasco_controller
con = nasco_controller.controller()


# --- freq params.
freq_1st_100ghz = 17.4452003333
freq_2nd_upper_100ghz = 9.5
freq_2nd_lower_100ghz = 4.0

freq_1st_200ghz = 18.764
freq_2nd_upper_200ghz = 4.0
freq_2nd_lower_200ghz = 6.6

# --- power params.
power_1st_100ghz = 14
power_2nd_upper_100ghz = 20
power_2nd_lower_100ghz = 20

power_1st_200ghz = 20
power_2nd_upper_200ghz = 14
power_2nd_lower_200ghz = 14


# OFF
#con.sg_100ghz_1st.set_onoff(0)
#con.sg_100ghz_2nd_upper.set_onoff(0)
#con.sg_100ghz_2nd_lower.set_onoff(0)
con.sg_200ghz_1st.set_onoff(0)
con.sg_200ghz_2nd_upper.set_onoff(0)
con.sg_200ghz_2nd_lower.set_onoff(0)
time.sleep(1)

# set_freq
#con.sg_100ghz_1st.set_freq(freq_1st_100ghz)
#con.sg_100ghz_2nd_upper.set_freq(freq_2nd_upper_100ghz)
#con.sg_100ghz_2nd_lower.set_freq(freq_2nd_lower_100ghz)
con.sg_200ghz_1st.set_freq(freq_1st_200ghz)
con.sg_200ghz_2nd_upper.set_freq(freq_2nd_upper_200ghz)
con.sg_200ghz_2nd_lower.set_freq(freq_2nd_lower_200ghz)
time.sleep(1)

# set_power
#con.sg_100ghz_1st.set_power(power_1st_100ghz)
#con.sg_100ghz_2nd_upper.set_power(power_2nd_upper_100ghz)
#con.sg_100ghz_2nd_lower.set_power(power_2nd_lower_100ghz)
#con.sg_200ghz_1st.set_power(power_1st_200ghz)
#con.sg_200ghz_2nd_upper.set_power(power_2nd_upper_200ghz)
#con.sg_200ghz_2nd_lower.set_power(power_2nd_lower_200ghz)
time.sleep(1)

# ON
#con.sg_100ghz_1st.set_onoff(1)
#con.sg_100ghz_2nd_upper.set_onoff(1)
#con.sg_100ghz_2nd_lower.set_onoff(1)
con.sg_200ghz_1st.set_onoff(1)
con.sg_200ghz_2nd_upper.set_onoff(1)
con.sg_200ghz_2nd_lower.set_onoff(1)
