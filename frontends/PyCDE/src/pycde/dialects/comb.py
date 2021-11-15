#  Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
#  See https://llvm.org/LICENSE.txt for license information.
#  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..value import wrap_opviews_with_values
from circt.dialects import comb

wrap_opviews_with_values(comb, __name__)
