import { InvalidRegistrationNumberError, RegistrationNumber } from '#src/register-student/domain/registration-number'

describe('RegistrationNumber', () => {
  it('Should preserve normalized registration number value when valid', () => {
    const registrationNumberInput: string = '1234567'
    const registrationNumberOutput: RegistrationNumber = RegistrationNumber.create('1234567')

    expect(RegistrationNumber.create(registrationNumberInput)).toStrictEqual(registrationNumberOutput)
  })

  it('should throw when registration number has more than 10 digits', () => {
    const registrationNumberInput: string = '12345679110'

    expect(() => RegistrationNumber.create(registrationNumberInput)).toThrow(InvalidRegistrationNumberError)
  })
})