from osgpypp import osg
import unittest
from numpy import arange

# osg.Matrix = osg.Matrixd
quat_scale = osg.Vec3d(1,1,1)

class TestQuat(unittest.TestCase):
    def test_quat(self):
        "Adapted from examples/osgunittests/osgunittests.cpp"
        q1 = osg.Quat()
        q1.makeRotate(osg.DegreesToRadians(30.0),0.0,0.0,1.0)

        q2 = osg.Quat()
        q2.makeRotate(osg.DegreesToRadians(133.0),0.0,1.0,1.0)

        q1_2 = q1*q2
        q2_1 = q2*q1

        m1 = osg.Matrix.rotate(q1)
        m2 = osg.Matrix.rotate(q2)
        
        m1_2 = m1*m2
        m2_1 = m2*m1
        
        qm1_2 = osg.Quat()
        qm1_2.set(m1_2)
        
        qm2_1 = osg.Quat()
        qm2_1.set(m2_1)
        
        print "q1*q2 = ", q1_2
        print "q2*q1 = ", q2_1
        print "m1*m2 = ", qm1_2
        print "m2*m1 = ", qm2_1

        testQuatRotate(osg.Vec3d(1.0,0.0,0.0),osg.Vec3d(0.0,1.0,0.0))
        testQuatRotate(osg.Vec3d(0.0,1.0,0.0),osg.Vec3d(1.0,0.0,0.0))
        testQuatRotate(osg.Vec3d(0.0,0.0,1.0),osg.Vec3d(0.0,1.0,0.0))
        testQuatRotate(osg.Vec3d(1.0,1.0,1.0),osg.Vec3d(1.0,0.0,0.0))
        testQuatRotate(osg.Vec3d(1.0,0.0,0.0),osg.Vec3d(1.0,0.0,0.0))
        testQuatRotate(osg.Vec3d(1.0,0.0,0.0),osg.Vec3d(-1.0,0.0,0.0))
        testQuatRotate(osg.Vec3d(-1.0,0.0,0.0),osg.Vec3d(1.0,0.0,0.0))
        testQuatRotate(osg.Vec3d(0.0,1.0,0.0),osg.Vec3d(0.0,-1.0,0.0))
        testQuatRotate(osg.Vec3d(0.0,-1.0,0.0),osg.Vec3d(0.0,1.0,0.0))
        testQuatRotate(osg.Vec3d(0.0,0.0,1.0),osg.Vec3d(0.0,0.0,-1.0))
        testQuatRotate(osg.Vec3d(0.0,0.0,-1.0),osg.Vec3d(0.0,0.0,1.0))

        # Test a range of rotations
        testGetQuatFromMatrix(quat_scale)

        # This is a specific test case for a matrix containing scale and rotation
        matrix = osg.Matrix(0.5, 0.0, 0.0, 0.0,
                           0.0, 0.5, 0.0, 0.0,
                           0.0, 0.0, 0.5, 0.0,
                           1.0, 1.0, 1.0, 1.0)
                           
        quat = osg.Quat()
        matrix.get(quat)
        
        print "Matrix = ", matrix, "rotation = ", quat, ", expected quat = (0,0,0,1)"

def testQuatRotate(from_quat, to):
    q_nicolas = osg.Quat()
    q_nicolas.makeRotate(from_quat,to)
    
    q_original = osg.Quat()
    q_original.makeRotate_original(from_quat,to)
    
    print "osg.Quat.makeRotate(", from_quat, ", ", to, ")"
    print "  q_nicolas = ", q_nicolas
    print "  q_original = ", q_original
    print "  from * M4x4(q_nicolas) = ", from_quat * osg.Matrixd.rotate(q_nicolas)
    print "  from * M4x4(q_original) = ", from_quat * osg.Matrixd.rotate(q_original)

# Exercise the Matrix.getRotate function.
# Compare the output of:
#  q1 * q2 
# versus
#  (mat(q1)*mat(q2)*scale).getRotate()
# for a range of rotations
def testGetQuatFromMatrix(scale):
    # Options
    
    # acceptable error range
    eps=1e-6

    # scale matrix
    # To not test with scale, use 1,1,1
    # Not sure if 0's or negative values are acceptable
    scalemat = osg.Matrixd()
    scalemat.makeScale(scale)
    
    # range of rotations
    if True:
        # wide range
        rol1start = 0.0
        rol1stop = 360.0
        rol1step = 20.0

        pit1start = 0.0
        pit1stop = 90.0
        pit1step = 20.0

        yaw1start = 0.0
        yaw1stop = 360.0
        yaw1step = 20.0

        rol2start = 0.0
        rol2stop = 360.0
        rol2step = 20.0

        pit2start = 0.0
        pit2stop = 90.0
        pit2step = 20.0

        yaw2start = 0.0
        yaw2stop = 360.0
        yaw2step = 20.0
    else:
        # focussed range
        rol1start = 0.0
        rol1stop = 0.0
        rol1step = 0.1

        pit1start = 0.0
        pit1stop = 5.0
        pit1step = 5.0

        yaw1start = 89.0
        yaw1stop = 91.0
        yaw1step = 0.0

        rol2start = 0.0
        rol2stop = 0.0
        rol2step = 0.0

        pit2start = 0.0
        pit2stop = 0.0
        pit2step = 0.1

        yaw2start = 89.0
        yaw2stop = 91.0
        yaw2step = 0.1
    #endif

    print "Starting testGetQuatFromMatrix, it can take a while ..."

    tstart = osg.Timer.instance().tick()
    count = 0
    for rol1 in arange(rol1start, rol1stop+1, rol1step):
        # for (double pit1 = pit1start pit1 <= pit1stop pit1 += pit1step) 
        for pit1 in arange(pit1start, pit1stop+1, pit1step):
            # for (double yaw1 = yaw1start yaw1 <= yaw1stop yaw1 += yaw1step) 
            for yaw1 in arange(yaw1start, yaw1stop+1, yaw1step):
                # for (double rol2 = rol2start rol2 <= rol2stop rol2 += rol2step) 
                for rol2 in arange(rol2start, rol2stop+1, rol2step):
                    # for (double pit2 = pit2start pit2 <= pit2stop pit2 += pit2step) 
                    for pit2 in arange(pit2start, pit2stop, pit2step):
                        # for (double yaw2 = yaw2start yaw2 <= yaw2stop yaw2 += yaw2step)
                        for yaw2 in arange(yaw2start, yaw2stop+1, yaw2step):
                        
                            count += 1
                            # create two quats based on the roll, pitch and yaw values
                            rot_quat1 = osg.Quat(
                                  osg.DegreesToRadians(rol1),osg.Vec3d(1,0,0),
                                  osg.DegreesToRadians(pit1),osg.Vec3d(0,1,0),
                                  osg.DegreesToRadians(yaw1),osg.Vec3d(0,0,1))

                            rot_quat2 = osg.Quat(
                                  osg.DegreesToRadians(rol2),osg.Vec3d(1,0,0),
                                  osg.DegreesToRadians(pit2),osg.Vec3d(0,1,0),
                                  osg.DegreesToRadians(yaw2),osg.Vec3d(0,0,1))

                            # create an output quat using quaternion math
                            out_quat1 = rot_quat2 * rot_quat1

                            # create two matrices based on the input quats
                            # osg.Matrixd mat1,mat2
                            mat1 = osg.Matrixd()
                            mat2 = osg.Matrixd()
                            mat1.makeRotate(rot_quat1)
                            mat2.makeRotate(rot_quat2)

                            # create an output quat by matrix multiplication and getRotate
                            out_mat = mat2 * mat1
                            # add matrix scale for even more nastiness
                            out_mat = out_mat * scalemat
                            out_quat2 = out_mat.getRotate()

                            # If the quaternion W is <0, then we should reflect
                            # to get it into the positive W.
                            # Unfortunately, when W is very small (close to 0), the sign
                            # does not really make sense because of precision problems
                            # and the reflection might not work.
                            if out_quat1.w()<0: 
                                out_quat1 = out_quat1 * -1.0
                            if out_quat2.w()<0: 
                                out_quat2 = out_quat2 * -1.0

                            # if the output quat length is not one 
                            # or if the components do not match,
                            # something is amiss

                            componentsOK = False
                            if ( ((abs(out_quat1.x()-out_quat2.x())) < eps) and
                                 ((abs(out_quat1.y()-out_quat2.y())) < eps) and
                                 ((abs(out_quat1.z()-out_quat2.z())) < eps) and
                                 ((abs(out_quat1.w()-out_quat2.w())) < eps) ):
                                    
                                componentsOK = True
                            
                            # We should also test for q = -q which is valid, so reflect
                            # one quat.
                            out_quat2 = out_quat2 * -1.0
                            if ( ((abs(out_quat1.x()-out_quat2.x())) < eps) and
                                 ((abs(out_quat1.y()-out_quat2.y())) < eps) and
                                 ((abs(out_quat1.z()-out_quat2.z())) < eps) and
                                 ((abs(out_quat1.w()-out_quat2.w())) < eps) ):
                                componentsOK = True
                            

                            lengthOK = False
                            if (abs(1.0-out_quat2.length()) < eps):
                                lengthOK = True
                            

                            if ( not lengthOK ) or ( not componentsOK ):
                                print ["testGetQuatFromMatrix problem at: \n"
                                     , " r1=", rol1
                                     , " p1=", pit1
                                     , " y1=", yaw1
                                     , " r2=", rol2
                                     , " p2=", pit2
                                     , " y2=", yaw2]
                                print "quats:        ", out_quat1, " length: ", out_quat1.length(), "\n"
                                print "mats and get: ", out_quat2, " length: ", out_quat2.length(), "\n\n"
    
    tstop = osg.Timer.instance().tick()
    duration = osg.Timer.instance().delta_s(tstart,tstop)
    print "Time for testGetQuatFromMatrix with ", count, " iterations: ", duration


if __name__ == '__main__':
    unittest.main()
