import numpy

"""
余弦相似度：
向量 A: [0.5, 0.5]
    B: [0.7, 0.7]
    C: [0.7, 0.5]
    D: [-0.6, -0.5]
    
公式：
    AB相似度：
        1.点积：(0.5 * 0.7 + 0.5 * 0.7)
        2.|A|：sqrt（0.5^2 + 0.5^2）
        3.|B|：sqrt（0.7^2 + 0.7^2）
        结果：(0.5 * 0.7 + 0.5 * 0.7) / (|A| * |B|) = 1.0
"""
# 计算两个向量的点积
def get_dot(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("两个向量必须维度数量相同")

    dot_sum = 0
    for a, b in zip(vector_a, vector_b):
        dot_sum += a * b

    return dot_sum

# 计算单个向量的模长：
def get_mod(vector):
    sum_square = 0
    for i in vector:
        sum_square += i * i

    # numpy.sqrt() 函数完成开根号
    return numpy.sqrt(sum_square)

# 计算余弦相似度：2 个向量的点积 / 两个向量的模长乘积
def cosine_similarity(vector_a, vector_b):
    return get_dot(vector_a, vector_b) / (get_mod(vector_a) * get_mod(vector_b))

# 主函数
if __name__ == '__main__':
    vector_a = [0.5, 0.5]
    vector_b = [0.7, 0.7]
    vector_c = [0.7, 0.5]
    vector_d = [-0.6, -0.5]

    print("ab: ", cosine_similarity(vector_a, vector_b))
    print("ac: ", cosine_similarity(vector_a, vector_c))
    print("ad: ", cosine_similarity(vector_a, vector_d))
