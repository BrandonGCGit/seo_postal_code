import postalCodesData from '../data/postal-codes.json';

export interface PostalCodeEntry {
  province: string;
  canton: string;
  district: string;
  postal_code: string;
}

export const postalCodes: PostalCodeEntry[] = postalCodesData;

/**
 * Gets all unique provinces
 */
export function getProvinces(): string[] {
  const provinces = [...new Set(postalCodes.map(entry => entry.province))];
  return provinces.sort();
}

/**
 * Gets all cantons for a specific province
 */
export function getCantonsByProvince(province: string): string[] {
  const cantons = [...new Set(
    postalCodes
      .filter(entry => entry.province === province)
      .map(entry => entry.canton)
  )];
  return cantons.sort();
}

/**
 * Gets all districts for a specific province and canton
 */
export function getDistrictsByCanton(province: string, canton: string): PostalCodeEntry[] {
  return postalCodes
    .filter(entry => entry.province === province && entry.canton === canton)
    .sort((a, b) => a.district.localeCompare(b.district));
}

/**
 * Gets all districts for a specific province
 */
export function getDistrictsByProvince(province: string): PostalCodeEntry[] {
  return postalCodes
    .filter(entry => entry.province === province)
    .sort((a, b) => a.district.localeCompare(b.district));
}

/**
 * Finds a specific district entry
 */
export function findDistrict(province: string, canton: string, district: string): PostalCodeEntry | undefined {
  return postalCodes.find(entry => 
    entry.province === province && 
    entry.canton === canton && 
    entry.district === district
  );
}

/**
 * Search postal codes by query (province, canton, district, or postal code)
 */
export function searchPostalCodes(query: string): PostalCodeEntry[] {
  const searchTerm = query.toLowerCase();
  return postalCodes.filter(entry =>
    entry.province.toLowerCase().includes(searchTerm) ||
    entry.canton.toLowerCase().includes(searchTerm) ||
    entry.district.toLowerCase().includes(searchTerm) ||
    entry.postal_code.includes(searchTerm)
  );
} 