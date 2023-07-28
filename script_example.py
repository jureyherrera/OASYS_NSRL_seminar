

import pandas as pd
import Shadow
import numpy


def run_shadow(roll_angle):

	# Python script to run shadow3. Created automatically with ShadowTools.make_python_script_from_list().
    #

    # write (1) or not (0) SHADOW files start.xx end.xx star.xx
    iwrite = 0
    
    #
    # initialize shadow3 source (oe0) and beam
    #
    beam = Shadow.Beam()
    oe0 = Shadow.Source()
    oe1 = Shadow.OE()
    oe2 = Shadow.OE()
    oe3 = Shadow.OE()
    oe4 = Shadow.OE()
    oe5 = Shadow.OE()
    oe6 = Shadow.OE()
    oe7 = Shadow.OE()
    oe8 = Shadow.OE()
    oe9 = Shadow.OE()
    oe10 = Shadow.OE()
    oe11 = Shadow.OE()
    oe12 = Shadow.OE()
    
    #
    # Define variables. See meaning of variables in: 
    #  https://raw.githubusercontent.com/srio/shadow3/master/docs/source.nml 
    #  https://raw.githubusercontent.com/srio/shadow3/master/docs/oe.nml
    #
    
    oe0.FDISTR = 3
    oe0.F_COLOR = 3
    oe0.F_PHOT = 0
    oe0.HDIV1 = 0.0
    oe0.HDIV2 = 0.0
    oe0.ISTAR1 = 0
    oe0.NPOINT = 500000
    oe0.PH1 = 6997.5
    oe0.PH2 = 7002.5
    oe0.SIGDIX = 7.843690679868878e-06
    oe0.SIGDIZ = 6.6362929020245845e-06
    oe0.SIGMAX = 3.070547765799666e-05
    oe0.SIGMAZ = 5.488850809206947e-06
    oe0.VDIV1 = 0.0
    oe0.VDIV2 = 0.0
    
    oe1.DUMMY = 100.0
    oe1.FWRITE = 3
    oe1.F_REFRAC = 2
    oe1.F_SCREEN = 1
    oe1.I_SLIT = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    oe1.N_SCREEN = 1
    oe1.RX_SLIT = numpy.array([0.00175, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe1.RZ_SLIT = numpy.array([0.0015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe1.T_IMAGE = 0.0
    oe1.T_INCIDENCE = 0.0
    oe1.T_REFLECTION = 180.0
    oe1.T_SOURCE = 27.2
    
    oe2.ALPHA = 90.0
    oe2.DUMMY = 100.0
    oe2.FHIT_C = 1
    oe2.FILE_REFL = b'Ni.dat'
    oe2.FWRITE = 3
    oe2.F_REFLEC = 1
    oe2.RLEN1 = 0.11
    oe2.RLEN2 = 0.11
    oe2.RWIDX1 = 0.04
    oe2.RWIDX2 = 0.04
    oe2.T_IMAGE = 0.0
    oe2.T_INCIDENCE = 89.5989295434
    oe2.T_REFLECTION = 89.5989295434
    oe2.T_SOURCE = 2.7
    
    oe3.ALPHA = 180.0
    oe3.DUMMY = 100.0
    oe3.FHIT_C = 1
    oe3.FILE_REFL = b'Ni.dat'
    oe3.FWRITE = 3
    oe3.F_REFLEC = 1
    oe3.RLEN1 = 0.484125
    oe3.RLEN2 = 0.484125
    oe3.RWIDX1 = 0.04
    oe3.RWIDX2 = 0.04
    oe3.T_IMAGE = 0.0
    oe3.T_INCIDENCE = 89.5989295434
    oe3.T_REFLECTION = 89.5989295434
    oe3.T_SOURCE = 0.825
    
    oe4.ALPHA = 90.0
    oe4.DUMMY = 100.0
    oe4.FWRITE = 3
    oe4.F_REFRAC = 2
    oe4.T_IMAGE = 0.0
    oe4.T_INCIDENCE = 0.0
    oe4.T_REFLECTION = 180.0
    oe4.T_SOURCE = 0.0
    
    oe5.DUMMY = 100.0
    oe5.FWRITE = 3
    oe5.F_REFRAC = 2
    oe5.F_SCREEN = 1
    oe5.I_SLIT = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    oe5.N_SCREEN = 1
    oe5.RX_SLIT = numpy.array([0.0015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe5.RZ_SLIT = numpy.array([0.0015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe5.T_IMAGE = 0.0
    oe5.T_INCIDENCE = 0.0
    oe5.T_REFLECTION = 180.0
    oe5.T_SOURCE = 5.475
    
    oe6.DUMMY = 100.0
    oe6.FHIT_C = 1
    oe6.FILE_REFL = b'Si2_40.111'
    oe6.FWRITE = 1
    oe6.F_CENTRAL = 1
    oe6.F_CRYSTAL = 1
    oe6.PHOT_CENT = 7000.0
    oe6.RLEN1 = 0.008
    oe6.RLEN2 = 0.072
    oe6.RWIDX1 = 0.005
    oe6.RWIDX2 = 0.005
    oe6.R_LAMBDA = 5000.0
    oe6.T_IMAGE = 0.0
    oe6.T_INCIDENCE = 73.5910617052
    oe6.T_REFLECTION = 73.5910617052
    oe6.T_SOURCE = 1.9
    
    oe7.ALPHA = 180.0
    oe7.DUMMY = 100.0
    oe7.FHIT_C = 1
    oe7.FILE_REFL = b'Si2_40.111'
    oe7.FWRITE = 1
    oe7.F_CENTRAL = 1
    oe7.F_CRYSTAL = 1
    oe7.PHOT_CENT = 7000.0
    oe7.RLEN1 = 0.008
    oe7.RLEN2 = 0.072
    oe7.RWIDX1 = 0.005
    oe7.RWIDX2 = 0.005
    oe7.R_LAMBDA = 5000.0
    oe7.T_IMAGE = 0.0
    oe7.T_INCIDENCE = 73.5910617052
    oe7.T_REFLECTION = 73.5910617052
    oe7.T_SOURCE = 0.012
    
    oe8.ALPHA = 180.0
    oe8.DUMMY = 100.0
    oe8.FWRITE = 3
    oe8.F_REFRAC = 2
    oe8.T_IMAGE = 0.0
    oe8.T_INCIDENCE = 0.0
    oe8.T_REFLECTION = 180.0
    oe8.T_SOURCE = 0.0
    
    oe9.CX_SLIT = numpy.array([5e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe9.DUMMY = 100.0
    oe9.FWRITE = 3
    oe9.F_REFRAC = 2
    oe9.F_SCREEN = 1
    oe9.I_SLIT = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    oe9.N_SCREEN = 1
    oe9.RX_SLIT = numpy.array([0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe9.RZ_SLIT = numpy.array([0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe9.T_IMAGE = 0.0
    oe9.T_INCIDENCE = 0.0
    oe9.T_REFLECTION = 180.0
    oe9.T_SOURCE = 12.888
    
    oe10.DUMMY = 100.0
    oe10.FCYL = 1
    oe10.FHIT_C = 1
    oe10.FILE_REFL = b'Ni.dat'
    oe10.FMIRR = 2
    oe10.FWRITE = 1
    oe10.F_DEFAULT = 0
    oe10.F_REFLEC = 1
    oe10.RLEN1 = 0.05
    oe10.RLEN2 = 0.05
    oe10.RWIDX1 = 0.015
    oe10.RWIDX2 = 0.015
    oe10.SIMAG = 0.15
    oe10.SSOUR = 51.5
    oe10.THETA = 89.654
    oe10.T_IMAGE = 0.0575
    oe10.T_INCIDENCE = 89.654
    oe10.T_REFLECTION = 89.654
    oe10.T_SOURCE = 0.5
    
    oe11.ALPHA = 90.0
    oe11.DUMMY = 100.0
    oe11.FCYL = 1
    oe11.FHIT_C = 1
    oe11.FILE_REFL = b'Ni.dat'
    oe11.FMIRR = 2
    oe11.FWRITE = 1
    oe11.F_DEFAULT = 0
    oe11.F_MOVE = 1
    oe11.F_REFLEC = 1
    oe11.RLEN1 = 0.025
    oe11.RLEN2 = 0.025
    oe11.RWIDX1 = 0.015
    oe11.RWIDX2 = 0.015
    oe11.SIMAG = 0.06
    oe11.SSOUR = 51.59
    oe11.THETA = 89.656
    oe11.T_IMAGE = 0.06
    oe11.T_INCIDENCE = 89.656
    oe11.T_REFLECTION = 89.656
    oe11.T_SOURCE = 0.0325
    oe11.Y_ROT = roll_angle #Roll
    
    oe12.ALPHA = 270.0
    oe12.DUMMY = 100.0
    oe12.FWRITE = 3
    oe12.F_REFRAC = 2
    oe12.T_IMAGE = 0.0
    oe12.T_INCIDENCE = 0.0
    oe12.T_REFLECTION = 180.0
    oe12.T_SOURCE = 0.0   
    
    
    #Run SHADOW to create the source
    
    if iwrite:
        oe0.write("start.00")
    
    beam.genSource(oe0)
    
    if iwrite:
        oe0.write("end.00")
        beam.write("begin.dat")
    
    
    #
    #run optical element 1
    #
    print("    Running optical element: %d"%(1))
    if iwrite:
        oe1.write("start.01")
    
    beam.traceOE(oe1,1)
    
    if iwrite:
        oe1.write("end.01")
        beam.write("star.01")
    
    
    #
    #run optical element 2
    #
    print("    Running optical element: %d"%(2))
    if iwrite:
        oe2.write("start.02")
    
    beam.traceOE(oe2,2)
    
    if iwrite:
        oe2.write("end.02")
        beam.write("star.02")
    
    
    #
    #run optical element 3
    #
    print("    Running optical element: %d"%(3))
    if iwrite:
        oe3.write("start.03")
    
    beam.traceOE(oe3,3)
    
    if iwrite:
        oe3.write("end.03")
        beam.write("star.03")
    
    
    #
    #run optical element 4
    #
    print("    Running optical element: %d"%(4))
    if iwrite:
        oe4.write("start.04")
    
    beam.traceOE(oe4,4)
    
    if iwrite:
        oe4.write("end.04")
        beam.write("star.04")
    
    
    #
    #run optical element 5
    #
    print("    Running optical element: %d"%(5))
    if iwrite:
        oe5.write("start.05")
    
    beam.traceOE(oe5,5)
    
    if iwrite:
        oe5.write("end.05")
        beam.write("star.05")
    
    
    #
    #run optical element 6
    #
    print("    Running optical element: %d"%(6))
    if iwrite:
        oe6.write("start.06")
    
    beam.traceOE(oe6,6)
    
    if iwrite:
        oe6.write("end.06")
        beam.write("star.06")
    
    
    #
    #run optical element 7
    #
    print("    Running optical element: %d"%(7))
    if iwrite:
        oe7.write("start.07")
    
    beam.traceOE(oe7,7)
    
    if iwrite:
        oe7.write("end.07")
        beam.write("star.07")
    
    
    #
    #run optical element 8
    #
    print("    Running optical element: %d"%(8))
    if iwrite:
        oe8.write("start.08")
    
    beam.traceOE(oe8,8)
    
    if iwrite:
        oe8.write("end.08")
        beam.write("star.08")
    
    
    #
    #run optical element 9
    #
    print("    Running optical element: %d"%(9))
    if iwrite:
        oe9.write("start.09")
    
    beam.traceOE(oe9,9)
    
    if iwrite:
        oe9.write("end.09")
        beam.write("star.09")
    
    
    #
    #run optical element 10
    #
    print("    Running optical element: %d"%(10))
    if iwrite:
        oe10.write("start.10")
    
    beam.traceOE(oe10,10)
    
    if iwrite:
        oe10.write("end.10")
        beam.write("star.10")
    
    
    #
    #run optical element 11
    #
    print("    Running optical element: %d"%(11))
    if iwrite:
        oe11.write("start.11")
    
    beam.traceOE(oe11,11)
    
    if iwrite:
        oe11.write("end.11")
        beam.write("star.11")
    
    
    #
    #run optical element 12
    #
    print("    Running optical element: %d"%(12))
    if iwrite:
        oe12.write("start.12")
    
    beam.traceOE(oe12,12)
    
    if iwrite:
        oe12.write("end.12")
        beam.write("star.12")
    
    
    return beam

def write_output(roll_angles):

	""" This function writes a CSV file with the horizontal and vertical FWHM
	for each rotation angle """

	df = pd.DataFrame(roll_angles, columns=['Rotation angle (deg)'])

	h_fwhm = []
	v_fwhm = []

	for roll_angle in roll_angles:
		
		beam = run_shadow(roll_angle)
		#Now we can get an histogram from the beam, more
		#https://github.com/oasys-kit/shadow3/blob/6b8270999a56c07176e19d66b5c6a587d129ac05/Shadow/ShadowLibExtensions.py#L691
		histo2 = beam.histo2(1, 3, nolost=1, nbins = 201)
		h_fwhm.append(histo2['fwhm_h'] * 1e6) # horizontal fwhm microns
		v_fwhm.append(histo2['fwhm_v'] * 1e6) # vertical fwhm microns

	df['Hor_FWHM(um)'] = h_fwhm
	df['Ver_FWHM(um)'] = v_fwhm

	df.to_csv('results_test.csv')
	print('results_test.csv has saved in disk')

if __name__=='__main__':

	roll_angles = numpy.linspace(-0.03, 0.03, 11)

	write_output(roll_angles)



