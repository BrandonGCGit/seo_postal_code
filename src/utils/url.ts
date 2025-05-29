/**
 * Sanitizes a string for use in URLs by removing accents, converting to lowercase,
 * and replacing spaces with hyphens
 */
export function sanitizeForUrl(text: string): string {
  return text
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // Remove accents
    .toLowerCase()
    .replace(/\s+/g, '-') // Replace spaces with hyphens
    .replace(/[^a-z0-9-]/g, '') // Remove special characters except hyphens
    .replace(/-+/g, '-') // Replace multiple hyphens with single hyphen
    .replace(/^-|-$/g, ''); // Remove leading/trailing hyphens
}

/**
 * Generates the URL path for a province
 */
export function getProvinceUrl(province: string): string {
  return `/codigo-postal/${sanitizeForUrl(province)}/`;
}

/**
 * Generates the URL path for a canton
 */
export function getCantonUrl(province: string, canton: string): string {
  return `/codigo-postal/${sanitizeForUrl(province)}/${sanitizeForUrl(canton)}/`;
}

/**
 * Generates the URL path for a district
 */
export function getDistrictUrl(province: string, canton: string, district: string): string {
  return `/codigo-postal/${sanitizeForUrl(province)}/${sanitizeForUrl(canton)}/${sanitizeForUrl(district)}/`;
}

/**
 * Generates WhatsApp share URL for a district
 */
export function getWhatsAppShareUrl(province: string, canton: string, district: string, postalCode: string): string {
  const message = `Código postal de ${district}, ${canton}, ${province}: ${postalCode}`;
  const encodedMessage = encodeURIComponent(message);
  return `https://wa.me/?text=${encodedMessage}`;
} 