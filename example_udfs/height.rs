// udf_type: Scalar
// id: count
// leaf_func: leaf
// mid_func: mid
// struct_name: Count

use petgraph::Graph;

struct ServiceName {
    fn leaf(my_node: String, graph: Graph) {
        return 0;
    }

    fn mid(my_node: String, graph: Graph) {
        return 1;
    }
}
