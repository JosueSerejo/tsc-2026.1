import { mock, type MockProxy } from 'vitest-mock-extended'

import type { GenerateId } from '#src/register-student/application/generate-id'
import type { LoadStudentByEmail } from '#src/register-student/application/load-student-by-email'
import type { LoadStudentByRegistrationNumber } from '#src/register-student/application/load-student-by-registration-number'
import type { RegisterStudentInput } from '#src/register-student/application/register-student-dtos'
import { RegisterStudentUseCase } from '#src/register-student/application/register-student-use-case'
import type { SaveStudent } from '#src/register-student/application/save-student'
import { Email } from '#src/register-student/domain/email'
import { RegistrationNumber } from '#src/register-student/domain/registration-number'

describe('RegisterStudentUseCase', () => {
  let input: RegisterStudentInput
  let loadStudentByemail: MockProxy<LoadStudentByEmail>
  let loadStudentByRegistrationNumber: MockProxy<LoadStudentByRegistrationNumber>
  let saveStudent: MockProxy<SaveStudent>
  let generateId: MockProxy<GenerateId>
  let sut: RegisterStudentUseCase

  beforeAll(() => {
    input = {
      name: 'Eyder Rios',
      email: 'eyderrios@email.com',
      registrationNumber: '1234517',
    }
    loadStudentByemail = mock<LoadStudentByEmail>()
    loadStudentByRegistrationNumber = mock<LoadStudentByRegistrationNumber>()
    saveStudent = mock<SaveStudent>()
    generateId = mock<GenerateId>()
    sut = new RegisterStudentUseCase(loadStudentByemail, loadStudentByRegistrationNumber, saveStudent, generateId)
  })

  it('Should call LoadStudentByEmail with provided email', async () => {
    loadStudentByemail.loadByEmail.mockResolvedValueOnce(null)
    loadStudentByRegistrationNumber.loadByRegistrationNumber.mockResolvedValueOnce(null)

    await sut.execute(input)

    expect(loadStudentByemail.loadByEmail).toHaveBeenCalledWith(Email.create(input.email))
  })

  // it('Should throw when email already exists', async () => {

  // })

  it('should compare equal registration numbers by value', () => {
    const firstRegistrationNumber = RegistrationNumber.create(input.registrationNumber)
    const secondRegistrationNumber = RegistrationNumber.create(input.registrationNumber)

    expect(firstRegistrationNumber.value).toBe(secondRegistrationNumber.value)
    
    expect(firstRegistrationNumber).not.toBe(secondRegistrationNumber)
  })


})