import axios from 'axios'

export const fetchAnalysisResults = (params) => {
  return axios.get('http://localhost:8000/api/v1/analysis/analyze', { params })
}
