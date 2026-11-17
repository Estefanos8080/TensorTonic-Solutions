
import numpy as np

def conv2d(x: list, W: list, b: list) -> np.ndarray:
    """
    Returns the convolved batch as a floating-point NumPy array.
    """
    x = np.array(x, dtype=float)
    W = np.array(W, dtype=float)
    b = np.array(b, dtype=float)

    stride = 1

    batch, in_channels, height, width = x.shape
    out_channels, _, kh, kw = W.shape

    out_height = (height - kh) // stride + 1
    out_width = (width - kw) // stride + 1

    D4_list = []

    for n in range(batch):
        batch_list = []

        for f in range(out_channels):
            filter_list = []

            for i in range(out_height):
                row_list = []

                for j in range(out_width):
                    patch = x[
                        n,
                        :,
                        i * stride:i * stride + kh,
                        j * stride:j * stride + kw
                    ]
                    result = np.dot(
                        patch.flatten(),
                        W[f].flatten()
                    )
                    result += b[f]

                    row_list.append(result)

                filter_list.append(row_list)

            batch_list.append(filter_list)

        D4_list.append(batch_list)

    return np.array(D4_list, dtype=float)
