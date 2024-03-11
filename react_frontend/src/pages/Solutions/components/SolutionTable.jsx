import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import './SolutionTable.css'

function SolutionTable({ solutions }) {
  return (
    <TableContainer component={Paper} sx={{
      width: '80%',
      '@media (prefers-color-scheme: dark)': {
        bgcolor: '#ffffff',
        color: '#213547',

      }
    }}>
      <Table stickyHeader aria-label="solutions table">
        <TableHead>
          <TableRow sx={{
            '@media (prefers-color-scheme: dark)': {
              bgcolor: '#1a1a1a',
              '& .MuiTableCell-head': {
                color: 'white',

              },
            }, fontSize: 'larger',

          }}>
            <TableCell sx={{
              '@media (prefers-color-scheme: dark)': {
                bgcolor: '#1a1a1a',
                color: 'white',
              },
            }}>Title</TableCell>
            <TableCell align="right" sx={{
              '@media (prefers-color-scheme: dark)': {
                bgcolor: '#1a1a1a',
                color: 'white',
              },
            }}>Difficulty</TableCell>
            <TableCell align="right" sx={{
              '@media (prefers-color-scheme: dark)': {
                bgcolor: '#1a1a1a',
                color: 'white',
              },
            }}>Companies</TableCell>
            <TableCell align="right" sx={{
              '@media (prefers-color-scheme: dark)': {
                bgcolor: '#1a1a1a',
                color: 'white',
              },
            }}>Programming Languages</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {solutions.map((solution) => (
            <TableRow
              key={solution.title}
              sx={{
                '&:last-child td, &:last-child th': { border: 0 },
                '@media (prefers-color-scheme: dark)': {
                  bgcolor: '#222',
                },
              }}
            >
              <TableCell component="th" scope="row" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}>
                {solution.title}
              </TableCell>
              <TableCell align="right" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}
              >{solution.difficulty}</TableCell>
              <TableCell align="right" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}>
                {solution.companies.map(company => company.name).join(", ")}
              </TableCell>
              <TableCell align="right" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}>
                {solution.programming_languages.map(language => language.name).join(", ")}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default SolutionTable;
