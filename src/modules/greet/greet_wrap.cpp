#include <boost/python.hpp>
#include "greet.h"

BOOST_PYTHON_MODULE(greet)
{
    using namespace boost::python;
    def("greet", greet);
}

