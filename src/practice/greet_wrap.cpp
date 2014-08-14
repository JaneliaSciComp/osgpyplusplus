#include <boost/python.hpp>
#include "greet.cpp"

BOOST_PYTHON_MODULE(greet)
{
    using namespace boost::python;
    def("greet", greet);
}

