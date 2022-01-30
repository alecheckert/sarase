#include <sarase.h>

PYBIND11_MODULE(_sarase, m) {
    m.def("add", &add);
}
