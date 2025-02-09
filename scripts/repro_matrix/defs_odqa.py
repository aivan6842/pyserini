#
# Pyserini: Reproducible IR research with sparse and dense representations
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# The models: the rows of the results table will be ordered this way.
models = {
    'models':
    ['BM25-k1_0.9_b_0.4',
     'BM25-k1_0.9_b_0.4_dpr-topics',
     'GarT5-RRF',
     'DPR',
     'DPR-DKRR',
     'DPR-Hybrid',
     'GarT5RRF-DKRR-RRF'
     ]
}

evaluate_dpr_retrieval_metric_definitions = {
        'Top5-1000': '--topk 5 20 100 500 1000',
        'Top5-100': '--topk 5 20 100'
}
